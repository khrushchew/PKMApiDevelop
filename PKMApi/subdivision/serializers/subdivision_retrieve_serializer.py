from rest_framework import serializers

from Core.models.Subdivision import Subdivision

class SubdivisionRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subdivision
        fields = ('name', )
