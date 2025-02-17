from rest_framework import viewsets

from .models import Website, SiteStatus
from .serializers import WebsiteSerializer, SiteStatusSerializer


class WebsiteViewSet(viewsets.ModelViewSet):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer

class SiteStatusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SiteStatus.objects.all()
    serializer_class = SiteStatusSerializer