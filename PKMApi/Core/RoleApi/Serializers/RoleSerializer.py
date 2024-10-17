from rest_framework import serializers

from Core.models.Role import Role


class RoleApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('pk', 'name', )
