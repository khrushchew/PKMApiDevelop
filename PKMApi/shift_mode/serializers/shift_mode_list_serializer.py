from  rest_framework import serializers

from Core.models.ShiftMode import ShiftMode


class ShiftModeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShiftMode
        fields = ('code', 'work_hours_per_day', 'shifts_per_day', 'hours_in_shifts', 'work_days_inline', 'weekends_inline', 'shift_working_day_mode', 'work_days_per_week', 'name')
