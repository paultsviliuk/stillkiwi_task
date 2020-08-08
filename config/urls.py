from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


swagger_view = get_schema_view(
   openapi.Info(
      title="Swagger UI",
      default_version='0.1'
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    path('swagger/', swagger_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', swagger_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


    # API urls
    path('api/', include(([
        # Your stuff: custom urls includes go here
        path(
            'redirects_analyzer/',
            include('redirects_analyzer.urls'),
            name="redirects_analyzer",
        ),
    ], 'api'), namespace='api')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Admin Site Config
admin.sites.AdminSite.site_header = settings.ADMIN_SITE_HEADER
admin.sites.AdminSite.site_title = settings.ADMIN_SITE_TITLE
