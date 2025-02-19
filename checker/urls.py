from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import WebsiteViewSet, SiteStatusViewSet

app_name = 'checker'


router = DefaultRouter()
router.register(r'websites', WebsiteViewSet, basename='website')
router.register(r'status', SiteStatusViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('check-site-status/', WebsiteViewSet.as_view({'post': 'create'}), name='check_site_status'),
]
