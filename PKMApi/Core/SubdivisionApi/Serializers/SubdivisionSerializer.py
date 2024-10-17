from rest_framework import serializers
from Core.models.Subdivision import Subdivision

class SubdivisionApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subdivision
        fields = ('pk', 'name', )
