from rest_framework import serializers

from Core.models.Department import Department
from Core.models.MachineName import MachineName
from Core.models.User import User

from Core.models.Allocation import Allocation


class DepartmentListSerializer(serializers.ModelSerializer):
    machines = serializers.SerializerMethodField(method_name='get_machines')
    masters = serializers.SerializerMethodField(method_name='get_masters')
    operators = serializers.SerializerMethodField(method_name='get_operators')

    class Meta:
        model = Department
        fields = ('pk', 'indent', 'name', 'main_user', 'machines', 'masters', 'operators')
    
    def get_machines(self, obj):
        return MachineName.objects.filter(area__department=obj).count()
    
    def get_masters(self, obj):
        try:
            master = Allocation.objects.filter(group__name='Мастер', department=obj)
        except:
            return 0
        return master.values('user').distinct().count()
    
    def get_operators(self, obj):
        try:
            operator = Allocation.objects.filter(group__name='Оператор', department=obj)
        except:
            return 0
        return operator.values('user').distinct().count()
