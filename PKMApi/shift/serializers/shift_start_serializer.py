from rest_framework import serializers

from Core.models.User import User


class ShiftStartSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('start_shift', )
        