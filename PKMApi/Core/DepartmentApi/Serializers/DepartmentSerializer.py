from rest_framework import serializers

from Core.models.Department import Department


class DepartmentApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('pk', 'indent', 'name', 'main_user')