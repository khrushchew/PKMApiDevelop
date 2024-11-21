from django.urls import include, path, re_path
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
from .MachineGroupApi.Views.MachineGroupViewSet import MachineGroupApiViewSet
from .MachineTypeApi.Views.MachineTypeViewSet import MachineTypeApiViewSet
from .MachineControlMethodApi.Views.MachineControlMethodView import MachineControlMethodApiViewSet
from .MachineNameApi.Views.MachineNameViewSet import MachineNameApiViewSet
from .BrigadeApi.Views.BrigadeViewSet import BrigadeApiViewSet

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

# MachineGroup
machine_group_router = routers.SimpleRouter()
machine_group_router.register(r'machinegroups', MachineGroupApiViewSet, basename='machinegroup')

# MachineType
machine_type_router = routers.SimpleRouter()
machine_type_router.register(r'machinetypes', MachineTypeApiViewSet, basename='machinetype')

# MachineControlMethod
machine_control_method_router = routers.SimpleRouter()
machine_control_method_router.register(r'machinecontrolmethods', MachineControlMethodApiViewSet, basename='machinecontrolmethod')

# MachineName
machine_name_router = routers.SimpleRouter()
machine_name_router.register(r'machinenames', MachineNameApiViewSet, basename='machinename')

# Brigade
brigade_router = routers.SimpleRouter()
brigade_router.register(r'brigades', BrigadeApiViewSet, basename='brigade')

urlpatterns=[

    path('login/', include('Core.LoginApi.LoginUrls')),
    path('logout/', include('Core.LogoutApi.LogoutUrls')),

    path('about/', AboutApiViewSet.as_view({'get': 'list'})),

    path('sys/', include('BIG_CALENDAR_API.urls')),

    # Subdivision
    path('<str:company_code>/', include(subdivision_router.urls)),

    # Role
    path('', include(role_router.urls)),

    #Platform
    path('', include(platform_router.urls)),

    # Department
    path('', include(department_router.urls)),

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

    # MachineGroup
    path('<str:company_code>/', include(machine_group_router.urls)),

    # MachineType
    path('<str:company_code>/', include(machine_type_router.urls)),

    # MachineControlMethod
    path('<str:company_code>/', include(machine_control_method_router.urls)),

    # MachineName
    path('<str:company_code>/', include(machine_name_router.urls)),

    # MachineName
    path('<str:company_code>/', include(brigade_router.urls)),
]

