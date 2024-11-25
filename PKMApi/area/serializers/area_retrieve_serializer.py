from rest_framework import serializers

from Core.models.Area import Area


class AreaRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('pk', 'indent', 'name')
