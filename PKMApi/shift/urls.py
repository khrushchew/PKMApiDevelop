from django.urls import path

from shift.swagger.shift_start_swagger import ShiftStartSwaggerView

urlpatterns = [
    path('start/', ShiftStartSwaggerView.as_view({'put': 'update'}))
]
