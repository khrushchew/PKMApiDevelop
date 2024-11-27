from django.urls import include, path

urlpatterns=[

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

    # Role
    # path('', include(role_router.urls)),

    # ShiftWorkingDayMode
    # path('<str:company_code>/', include(shift_working_day_mode_router.urls)),

    # ShiftMode
    # path('<str:company_code>/', include(shift_mode_router.urls)),

    # ShiftCalendar
    # path('<str:company_code>/', include(shift_calendar_router.urls)),

    # MachineStyle
    # path('<str:company_code>/', include(machine_style_router.urls)),

    # MachineGroup
    # path('<str:company_code>/', include(machine_group_router.urls)),

    # MachineType
    # path('<str:company_code>/', include(machine_type_router.urls)),

    # MachineControlMethod
    # path('<str:company_code>/', include(machine_control_method_router.urls)),

    # MachineName
    # path('<str:company_code>/', include(machine_name_router.urls)),

    # MachineName
    # path('<str:company_code>/', include(brigade_router.urls)),
]

