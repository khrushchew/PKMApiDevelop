from rest_framework import serializers

from Core.models.Area import Area
from Core.models.MachineName import MachineName
from Core.models.Allocation import Allocation


class AreaListSerializer(serializers.ModelSerializer):
    machines = serializers.SerializerMethodField(method_name='get_machines')
    masters = serializers.SerializerMethodField(method_name='get_masters')
    operators = serializers.SerializerMethodField(method_name='get_operators')

    class Meta:
        model = Area
        fields = ('pk', 'indent', 'name', 'machines', 'masters', 'operators')
    
    def get_machines(self, obj):
        return MachineName.objects.filter(area=obj).count()
    
    def get_masters(self, obj):
        try:
            master = Allocation.objects.filter(group__name='Мастер', area=obj)
        except:
            return 0
        return master.values('user').distinct().count()
    
    def get_operators(self, obj):
        try:
            operator = Allocation.objects.filter(group__name='Оператор', area=obj)
        except:
            return 0
        return operator.values('user').distinct().count()
    