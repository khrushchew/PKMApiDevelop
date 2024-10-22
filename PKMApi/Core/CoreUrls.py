from django.urls import include, path
from rest_framework import routers

from .SubdivisionApi.Views.SubdivisionViewSet import SubdivisionApiViewSet
from .RoleApi.Views.RoleViewSet import RoleApiViewSet
from .PlatformApi.Views.PlatformViewSet import PlatformApiViewSet
from .DepartmentApi.Views.DepartmentViewSet import DepartmentApiViewSet
from .AreaApi.Views.AreaApiViewSet import  AreaApiViewSet

# Subdivision
subdivision_router = routers.SimpleRouter()
subdivision_router.register(r'subdivisions', SubdivisionApiViewSet, basename='subdivision')

# Role
role_router = routers.SimpleRouter()
role_router.register(r'roles', RoleApiViewSet, basename='role')

# Platform
platform_router = routers.SimpleRouter()
platform_router.register(r'platforms', PlatformApiViewSet, basename='platform')

# Department
department_router = routers.SimpleRouter()
department_router.register(r'departments', DepartmentApiViewSet, basename='department')

# Area
area_router = routers.SimpleRouter()
area_router.register(r'areas', AreaApiViewSet, basename='area')

urlpatterns=[
    path('auth/', include('Core.AuthApi.AuthUrls')),

    # Subdivision
    path('<str:company_code>/', include(subdivision_router.urls)),

    # Role
    path('<str:company_code>/', include(role_router.urls)),

    #Platform
    path('<str:company_code>/', include(platform_router.urls)),

    # Department
    path('<str:company_code>/', include(department_router.urls)),

    # Area
    path('<str:company_code>/', include(area_router.urls)),
]