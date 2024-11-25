from django.urls import include, path

from rest_framework import routers

from .views.department_view import DepartmentViewSet

department_router = routers.SimpleRouter()
department_router.register(r'', DepartmentViewSet, 'department')

urlpatterns = [
    path('v1/', include(department_router.urls))
]
