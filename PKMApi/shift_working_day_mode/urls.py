from django.urls import path, include

from rest_framework import routers

from shift_working_day_mode.swagger.shift_working_day_mode_swagger import ShiftWorkingDayModeSwaggerView

shift_working_day_mode_router = routers.SimpleRouter()
shift_working_day_mode_router.register(r'', ShiftWorkingDayModeSwaggerView, 'shift_working_day_mode')

urlpatterns = [
    path('v1/', include(shift_working_day_mode_router.urls))
]
