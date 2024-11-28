from django.urls import path, include

from rest_framework import routers

from shift_working_day_mode.views.shift_working_day_mode_view import ShiftWorkingDayModeView

shift_working_day_mode_router = routers.SimpleRouter()
shift_working_day_mode_router.register(r'', ShiftWorkingDayModeView, 'shift_working_day_mode')

urlpatterns = [
    path('v1/', include(shift_working_day_mode_router.urls))
]
