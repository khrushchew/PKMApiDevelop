from django.urls import path, include
from rest_framework import routers

from machine_group.swagger.machine_group_swagger import MachineGroupSwaggerView

machine_group_router = routers.SimpleRouter()
machine_group_router.register('', MachineGroupSwaggerView, 'machine_group')

urlpatterns = [
    path('v1/', include(machine_group_router.urls))
]
