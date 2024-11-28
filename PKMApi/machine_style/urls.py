from django.urls import path, include
from rest_framework import routers

from machine_style.swagger.machine_style_swagger import MachineStyleSwaggerView

machine_style_router = routers.SimpleRouter()
machine_style_router.register(f'', MachineStyleSwaggerView, 'machine_style')

urlpatterns = [
    path('v1/', include(machine_style_router.urls))
]