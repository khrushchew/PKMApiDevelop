from django.urls import include, path

urlpatterns=[
    path('auth/', include('Core.AuthApi.AuthUrls')),

    path('subdivisions/', include('Core.SubdivisionApi.SubdivisionUrls')),

    path('roles/', include('Core.RoleApi.RoleUrls')),

    path('platforms/', include('Core.PlatformApi.PlatformUrls')),
]