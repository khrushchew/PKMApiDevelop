from  rest_framework import serializers

from Core.models.ShiftMode import ShiftMode


class ShiftModeApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShiftMode
        fields = '__all__'