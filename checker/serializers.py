from rest_framework import serializers

from .models import Website, SiteStatus

class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = '__all__'


class SiteStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteStatus
        fields = '__all__'