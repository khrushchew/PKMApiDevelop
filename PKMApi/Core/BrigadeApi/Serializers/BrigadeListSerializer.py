from rest_framework import serializers

from Core.models.Brigade import Brigade

class BrigadeListApiSerializer(serializers.ModelSerializer):
    area = serializers.StringRelatedField()
    shift_mode = serializers.StringRelatedField()

    department = serializers.SerializerMethodField(method_name='get_department')
    name_shift_mode = serializers.SerializerMethodField(method_name='get_name_shift_mode')

    class Meta:
        model = Brigade
        fields = ('pk', 'code', 'name', 'department', 'area', 'shift_mode', 'name_shift_mode')
    
    def get_department(self, obj):
        return obj.area.department.name
    
    def get_name_shift_mode(self, obj):
        return obj.shift_mode.name