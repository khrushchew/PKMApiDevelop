from django.urls import include, path

from rest_framework import routers

from .swagger.department_swagger import DepartmentSwaggerView

department_router = routers.SimpleRouter()
department_router.register(r'', DepartmentSwaggerView, 'department')

urlpatterns = [
    path('v1/', include(department_router.urls))
]
