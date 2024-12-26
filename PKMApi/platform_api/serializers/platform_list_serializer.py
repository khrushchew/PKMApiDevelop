from rest_framework import serializers

from Core.models.Platform import Platform
from Core.models.MachineName import MachineName
from Core.models.Allocation import Allocation

from django.contrib.auth.models import Group

from drf_yasg.utils import swagger_serializer_method


class PlatformListSerializer(serializers.ModelSerializer):
    machines = serializers.SerializerMethodField(method_name='get_machines')
    masters = serializers.SerializerMethodField(method_name='get_masters')
    operators = serializers.SerializerMethodField(method_name='get_operators')

    class Meta:
        model = Platform
        fields = ('pk', 'indent', 'name', 'address', 'machines', 'masters', 'operators')

    @swagger_serializer_method(serializer_or_field=serializers.IntegerField)
    def get_machines(self, obj):
        return MachineName.objects.filter(area__department__platform=obj).count()
    
    @swagger_serializer_method(serializer_or_field=serializers.IntegerField)
    def get_masters(self, obj):
        try:
            master = Allocation.objects.filter(group__name='Мастер', platform=obj)
        except:
            return 0
        return master.values('user').distinct().count()
    
    @swagger_serializer_method(serializer_or_field=serializers.IntegerField)
    def get_operators(self, obj):
        try:
            operator = Allocation.objects.filter(group__name='Оператор', platform=obj)
        except:
            return 0
        return operator.values('user').distinct().count()
