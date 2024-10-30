from rest_framework import serializers

from Core.models.ShiftCalendar import ShiftCalendar


class ShiftCalendarApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShiftCalendar
        fields = ('pk', 'day', 'shift_working_day_mode', 'shift_mode')
        