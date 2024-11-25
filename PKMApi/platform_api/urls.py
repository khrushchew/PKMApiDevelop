from django.urls import include, path

from rest_framework import routers

from .swagger.platform_swagger import PlatformSwaggerView

platform_router = routers.SimpleRouter()
platform_router.register(r'', PlatformSwaggerView, 'platform')

urlpatterns = [
    path('v1/', include(platform_router.urls))
]
