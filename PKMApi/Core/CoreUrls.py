from django.urls import include, path
from django.contrib import admin

from PKMApi.yasg import urlpatterns as doc_urls
from django.views.generic.base import RedirectView

urlpatterns=[
    
    path('', RedirectView.as_view(url='/admin/', permanent=True)),
    path('admin/', admin.site.urls),

    path('login/', include('app_auth.urls')),

    path('logout/', include('logout.urls')),

    path('about/', include('about.urls')),

    path('sys/', include('BIG_CALENDAR.urls')),

    #Platform
    path('platforms/', include('platform_api.urls')),

    # Department
    path('departments/', include('department.urls')),

    # Area
    path('areas/', include('area.urls')),

    # Subdivision
    path('subdivisions/', include('subdivision.urls')),

    # Shift
    path('shifts/', include('shift.urls')),

    # MachineStyle
    path('machine_styles/', include('machine_style.urls')),

    # MachineGroup
    path('machine_groups/', include('machine_group.urls')),

    # Role
    # path('', include(role_router.urls)),

    # ShiftWorkingDayMode
    path('shift_working_day_modes/', include('shift_working_day_mode.urls')),

    # ShiftMode
    path('shift_modes/', include('shift_mode.urls')),

    # ShiftCalendar
    # path('<str:company_code>/', include(shift_calendar_router.urls)),



    

    # MachineType
    # path('<str:company_code>/', include(machine_type_router.urls)),

    # MachineControlMethod
    # path('<str:company_code>/', include(machine_control_method_router.urls)),

    # MachineName
    # path('<str:company_code>/', include(machine_name_router.urls)),

    # MachineName
    # path('<str:company_code>/', include(brigade_router.urls)),
]

urlpatterns += doc_urls
