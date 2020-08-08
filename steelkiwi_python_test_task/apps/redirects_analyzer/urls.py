from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter
from redirects_analyzer.views import RedirectDataViewSet


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('redirect', RedirectDataViewSet, basename="redirect")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls))
]
