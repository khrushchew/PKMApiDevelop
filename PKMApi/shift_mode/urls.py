from django.urls import include, path

from rest_framework import routers

from shift_mode.swagger.shift_mode_swagger import ShiftModeSwaggerView

shift_mode_router = routers.SimpleRouter()
shift_mode_router.register(r'shift_modes', ShiftModeSwaggerView, 'shift_mode')


urlpatterns = [
    path('v1/', include(shift_mode_router.urls))
]
