from django.contrib import admin

from redirects_analyzer.models import RedirectData


@admin.register(RedirectData)
class RedirectModelAdmin(admin.ModelAdmin):
    search_fields = ('redirect_domain', 'referrer_domain')
    list_display = ('redirect_url', 'referrer_domain', 'browser', 'os', 'created_at')
