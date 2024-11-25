from rest_framework import serializers

from Core.models.Department import Department
from Core.models.MachineName import MachineName
from Core.models.User import User

from django.contrib.auth.models import Group


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
            master = Group.objects.get(name='Мастер')
        except:
            return 0
        return User.objects.filter(groups=master).count()
    
    def get_operators(self, obj):
        try:
            operator = Group.objects.get(name='Оператор')
        except:
            return 0
        return User.objects.filter(groups=operator).count()
