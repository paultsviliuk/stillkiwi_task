from datetime import datetime

from django.http import HttpResponseRedirect
from django.db.models import Count, Max, F
from django.contrib.postgres.aggregates import ArrayAgg
from django.db import transaction
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

from redirects_analyzer.serializers import RedirectUrlSerializer, RedirectDataListSerializer, \
    RedirectDataTopListSerializer, RedirectDataListByDomainSerializer
from redirects_analyzer.models import RedirectData
from redirects_analyzer.tasks import store_redirect_data


class StandardResultsPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


class RedirectDataViewSet(mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          viewsets.GenericViewSet):
    """
    ViewSet to registering new redirects and getting redirects via lists for statistical analysis
    permission_classes - AllowAny
    """
    queryset = RedirectData.objects.all().order_by('created_at')
    permission_classes = (AllowAny,)
    serializer_class = RedirectUrlSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ['redirect_domain', 'referrer_domain', ]
    search_fields = ['redirect_domain', 'referrer_domain', ]
    ordering_fields = ['created_at', ]
    pagination_class = StandardResultsPagination

    def get_serializer_class(self):
        if self.action == 'create':
            return RedirectUrlSerializer
        elif self.action == 'top':
            return RedirectDataTopListSerializer
        elif self.action == 'by_domain':
            return RedirectDataListByDomainSerializer
        return RedirectDataListSerializer

    def create(self, request, *args, **kwargs):
        """
        Register new redirect.
        """
        with transaction.atomic():
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            redirect_to = serializer.validated_data['redirect_url']
            referrer = request.META.get('HTTP_REFERER', '')
            agent = request.META.get('HTTP_USER_AGENT')
            ip = request.META.get('REMOTE_ADDR')

            store_redirect_data.delay(redirect_to, referrer, ip, agent)
            return HttpResponseRedirect(redirect_to=redirect_to)

    def list(self, request, *args, **kwargs):
        """
        List of all performed redirects.
        """
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_domain(self, request, *args, **kwargs):
        """
        List of all performed redirects for certain redirect domain name.
        """
        result = RedirectData.objects\
            .annotate(redirect_full_url=F('redirect_url'))\
            .values('redirect_full_url')\
            .annotate(redirects=Count('redirect_full_url'),
                      referrers=ArrayAgg(
                          F('referrer_domain')
                      ),
                      last_redirected=Max('created_at'),
                      )
        queryset = self.filter_queryset(result)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def top(self, request, *args, **kwargs):
        """
        List of top 10 domains for which redirects were made this month
        """
        queryset = self.filter_queryset(self.get_queryset())
        current_month = datetime.today().month
        result = queryset.filter(
                            created_at__month=current_month
        ).values('redirect_domain').annotate(
            redirects_count=Count('redirect_domain'),
        ).order_by(
            '-redirects_count'
        )[:10]

        page = self.paginate_queryset(result)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(result, many=True)
        return Response(serializer.data)
