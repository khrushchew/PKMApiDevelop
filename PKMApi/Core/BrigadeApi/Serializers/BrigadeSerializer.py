from rest_framework import serializers

from Core.models.Brigade import Brigade
from Core.models.Area import Area

class BrigadeApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brigade
        fields = ('pk', 'company', 'code', 'name', 'area', 'shift_mode')
