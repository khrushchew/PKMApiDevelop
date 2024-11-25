from django.urls import path, include

from rest_framework import routers

from .swagger.area_swagger import AreaSwaggerView

area_router = routers.SimpleRouter()
area_router.register(r'', AreaSwaggerView, 'area')

urlpatterns = [
    path('v1/', include(area_router.urls)),
]
