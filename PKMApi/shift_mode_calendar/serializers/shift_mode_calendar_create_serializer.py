from rest_framework import serializers

from Core.models.ShiftModeCalendar import ShiftModeCalendar


class ShiftModeCalendarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = ShiftModeCalendar
        fields = ('day', 'shift_working_day_mode', 'shift_mode')
