from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated

from shift_mode_calendar.serializers.shift_mode_calendar_create_serializer import ShiftModeCalendarCreateSerializer


# class ShiftModeCalendarView(ViewSet):
    
#     permission_classes = [IsAuthenticated]

#     def create(self, request, *args, **kwargs):
        