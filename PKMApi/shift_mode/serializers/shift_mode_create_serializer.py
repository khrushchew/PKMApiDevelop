from  rest_framework import serializers

from Core.models.ShiftMode import ShiftMode


class ShiftModeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShiftMode
        fields = ('company', 'code', 'work_hours_per_day', 'shifts_per_day', 'hours_in_shifts', 'work_days_inline', 'weekends_inline', 'shift_working_day_mode', 'work_days_per_week', 'name')

    def validate_code(self, obj):
        if ShiftMode.objects.filter(code=obj, company=self.context.get('request').user.company).exists():
            raise serializers.ValidationError({'detail': 'Такой код режима сменности уже существует'}) 
        else:
            return obj
