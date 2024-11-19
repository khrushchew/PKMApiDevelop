from rest_framework import serializers

from Core.models.Department import Department


class DepartmentRetrieveApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('indent', 'name', 'main_user', 'platform')