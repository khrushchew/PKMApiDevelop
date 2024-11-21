from rest_framework import serializers

from django.contrib.auth.models import Group
from Core.models.Allocation import Allocation
from Core.models.Platform import Platform
from Core.models.Department import Department
from Core.models.Area import Area
from Core.models.Brigade import Brigade
from Core.models.Shift import Shift


class RoleCreateApiSerializer(serializers.ModelSerializer):
    department = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Department.objects.all(), write_only=True
    )
    area = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Area.objects.all(), write_only=True
    )
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all())
    platform = serializers.PrimaryKeyRelatedField(queryset=Platform.objects.all())
    brigade = serializers.PrimaryKeyRelatedField(queryset=Brigade.objects.all(), allow_null=True, required=False)
    shift = serializers.PrimaryKeyRelatedField(queryset=Shift.objects.all(), allow_null=True, required=False)

    class Meta:
        model = Allocation
        fields = ('user', 'group', 'platform', 'brigade', 'shift', 'department', 'area', )

    def create(self, validated_data):
        departments = validated_data.pop('department')
        areas = validated_data.pop('area')

        allocation = Allocation.objects.create(**validated_data)

        allocation.department.set(departments)
        allocation.area.set(areas)

        return allocation