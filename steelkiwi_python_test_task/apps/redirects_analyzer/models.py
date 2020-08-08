from django.db import models


class RedirectData(models.Model):
    """
    Model to store all the necessary data about all redirects
    """

    redirect_domain = models.CharField(max_length=256)
    redirect_url = models.URLField(max_length=2048)
    redirect_params = models.CharField(max_length=2048, blank=True, null=True)
    referrer_domain = models.CharField(max_length=256, blank=True, null=True)
    referrer_url = models.URLField(max_length=2048, blank=True, null=True)

    ip = models.GenericIPAddressField()
    browser = models.CharField(max_length=64, blank=True, null=True)
    os = models.CharField(max_length=64, blank=True, null=True)
    platform = models.CharField(max_length=64, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "redirect_data"

    def __str__(self):
        return self.redirect_url
