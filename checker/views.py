import requests

from rest_framework.response import Response
from django.utils.timezone import now
from rest_framework import viewsets

from .models import Website, SiteStatus
from .serializers import WebsiteSerializer, SiteStatusSerializer

class WebsiteViewSet(viewsets.ModelViewSet):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer

    def create(self, request, *args, **kwargs):
        url = request.data.get("url")
        if not url:
            return Response({"error": "URL is required"}, status=400)

        website, _ = Website.objects.get_or_create(url=url)
        try:
            response = requests.get(url, timeout=10)
            status_code = response.status_code
            response_time = response.elapsed.total_seconds()
        except requests.RequestException:
            status_code = None
            response_time = None

        site_status = SiteStatus.objects.create(
            website=website,
            status_code=status_code,
            response_time=response_time,
            checked_at=now()
        )

        return Response({
            "id": website.id,
            "url": website.url,
            "status_code": site_status.status_code,
            "response_time": site_status.response_time,
            "checked_at": site_status.checked_at,
        })

class SiteStatusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SiteStatus.objects.all()
    serializer_class = SiteStatusSerializer
