from django.db import models

class Website(models.Model):
    url = models.URLField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


class SiteStatus(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    status_code = models.IntegerField(null=True, blank=True)
    response_time = models.FloatField(null=True, blank=True)
    checked_at = models.DateTimeField(auto_now_add=True)