from django.urls import include, path

from rest_framework import routers

from .views.platform_view import PlatformViewSet

platform_router = routers.SimpleRouter()
platform_router.register(r'', PlatformViewSet, 'platform')

urlpatterns = [
    path('v1/', include(platform_router.urls))
]
