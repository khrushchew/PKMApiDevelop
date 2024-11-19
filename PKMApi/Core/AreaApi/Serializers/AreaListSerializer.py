from rest_framework import serializers

from Core.models.Area import Area
from Core.models.MachineName import MachineName
# from Core.models.RoleOperator import RoleOperator
# from Core.models.RoleMasterArea import RoleMasterArea


class AreaListApiSerializer(serializers.ModelSerializer):
    machines = serializers.SerializerMethodField(method_name='get_machines')
    masters = serializers.SerializerMethodField(method_name='get_masters')
    operators = serializers.SerializerMethodField(method_name='get_operators')

    class Meta:
        model = Area
        fields = ('pk', 'indent', 'name', 'machines', 'masters', 'operators')
    
    # def get_machines(self, obj):
    #     return MachineName.objects.filter(area=obj).count()
    
    # def get_masters(self, obj):
    #     return RoleMasterArea.objects.filter(area=obj).count()
    
    # def get_operators(self, obj):
    #     return RoleOperator.objects.filter(area=obj).count()