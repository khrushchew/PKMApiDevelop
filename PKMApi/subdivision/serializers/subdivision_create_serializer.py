from rest_framework import serializers

from Core.models.Subdivision import Subdivision


class SubdivisionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subdivision
        fields = ('name', 'company')
    
    def validate_name(self, value):
        if Subdivision.objects.filter(name=value, company=self.context.get('request').user.company).exists():
            raise serializers.ValidationError({'detail': 'Подразделение с таким названием уже существует'})
        else:
            return value
 