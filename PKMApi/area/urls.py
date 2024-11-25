from django.urls import path, include

from rest_framework import routers

from .views.area_view import AreaView

area_router = routers.SimpleRouter()
area_router.register(r'', AreaView, 'area')

urlpatterns = [
    path('v1/', include(area_router.urls)),
]
