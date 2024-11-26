from rest_framework import serializers

from Core.models.Subdivision import Subdivision

class SubdivisionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subdivision
        fields = ('name', )
