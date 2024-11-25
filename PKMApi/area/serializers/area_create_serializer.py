from rest_framework import serializers

from Core.models.Area import Area


class AreaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('indent', 'name', 'department')
