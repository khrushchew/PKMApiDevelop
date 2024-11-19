from rest_framework import serializers

from Core.models.Shift import Shift


class ShiftCreateApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = ('brigade', 'name')
