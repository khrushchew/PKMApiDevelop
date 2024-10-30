from django.urls import include, path
from rest_framework import routers

from .SubdivisionApi.Views.SubdivisionViewSet import SubdivisionApiViewSet
from .RoleApi.Views.RoleViewSet import RoleApiViewSet
from .PlatformApi.Views.PlatformViewSet import PlatformApiViewSet
from .DepartmentApi.Views.DepartmentViewSet import DepartmentApiViewSet
from .AreaApi.Views.AreaApiViewSet import  AreaApiViewSet
from .AboutApi.Views.AboutViewSet import AboutApiViewSet
from .ShiftWorkingDayModeApi.Views.ShiftWorkingDayModeViewSet import ShiftWorkingDayModeApiViewSet
from .ShiftModeApi.Views.ShiftModeViewSet import ShiftModeApiViewSet
from .ShiftCalendarApi.Views.ShiftCalendarViewSet import ShiftCalendarApiViewSet
from .MachineStyleApi.Views.MachineStyleViewSet import MachineStyleApiViewSet

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

# ShiftWorkingDayMode
shift_working_day_mode_router = routers.SimpleRouter()
shift_working_day_mode_router.register(r'shiftworkingdaymodes', ShiftWorkingDayModeApiViewSet, basename='shiftworkingdaymode')

# ShiftMode
shift_mode_router = routers.SimpleRouter()
shift_mode_router.register(r'shiftmodes', ShiftModeApiViewSet, basename='shiftmode')

# ShiftCalendar
shift_calendar_router = routers.SimpleRouter()
shift_calendar_router.register(r'shiftcalendars', ShiftCalendarApiViewSet, basename='shiftcalendar')

# MachineStyle
machine_style_router = routers.SimpleRouter()
machine_style_router.register(r'machinestyles', MachineStyleApiViewSet, basename='machinestyle')

urlpatterns=[
    path('about/', AboutApiViewSet.as_view({'get': 'list'})),

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

    # ShiftWorkingDayMode
    path('<str:company_code>/', include(shift_working_day_mode_router.urls)),

    # ShiftMode
    path('<str:company_code>/', include(shift_mode_router.urls)),

    # ShiftCalendar
    path('<str:company_code>/', include(shift_calendar_router.urls)),

    # MachineStyle
    path('<str:company_code>/', include(machine_style_router.urls)),
]