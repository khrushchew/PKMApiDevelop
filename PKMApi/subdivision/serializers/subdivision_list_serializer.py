from rest_framework import serializers

from Core.models.Subdivision import Subdivision
from Core.models.User import User

class SubdivisionListSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField(method_name='get_users')

    class Meta:
        model = Subdivision
        fields = ('id', 'name', 'users')
    
    def get_users(self, obj):
        return User.objects.filter(subdivision=obj).count()
