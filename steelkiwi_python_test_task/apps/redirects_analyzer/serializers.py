from rest_framework import serializers

from .models import RedirectData


class RedirectUrlSerializer(serializers.ModelSerializer):
    redirect_url = serializers.URLField()

    class Meta:
        model = RedirectData
        fields = ('redirect_url', )


class RedirectDataListSerializer(serializers.ModelSerializer):

    class Meta:
        model = RedirectData
        fields = '__all__'


class RedirectDataTopListSerializer(serializers.ModelSerializer):
    redirects_count = serializers.IntegerField()
    redirect_domain = serializers.CharField()

    class Meta:
        model = RedirectData
        fields = ('redirect_domain', 'redirects_count', )


class RedirectDataListByDomainSerializer(serializers.ModelSerializer):
    redirects = serializers.IntegerField()
    redirect_full_url = serializers.CharField()
    referrers = serializers.StringRelatedField(many=True)
    last_redirected = serializers.DateTimeField()

    class Meta:
        model = RedirectData
        fields = ('redirect_full_url', 'redirects', 'referrers', 'last_redirected', )
