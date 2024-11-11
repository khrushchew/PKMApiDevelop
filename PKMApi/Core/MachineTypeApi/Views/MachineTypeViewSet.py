from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.exceptions import NotFound, ValidationError

from ..Serializers.MachineTypeSerializer import MachineTypeApiSerializer

from Core.models.MachineType import MachineType

from Core.models.MachineGroup import MachineGroup
from Core.models.MachineName import MachineName

class MachineTypeApiViewSet(ViewSet):

    handler200 = Response(status=200)
    handler201 = Response(status=201)
    handler204 = Response(status=204)
    handler500 = Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    def get_machine_group(self):
        machine_group = self.request.data.get('group')
        try:
            return MachineGroup.objects.get(name=machine_group)
        except:
            raise NotFound({'error': 'Такой группы оборудования не найдено'})
        
    def check_name(self):
        if MachineType.objects.filter(group__style__company__code=self.kwargs.get('company_code'), group=self.request.data.get('group'), name=self.request.data.get('name')).exists():
            raise ValidationError({'error': 'Тип оборудования с таким названием уже существует'})

    def get_machine_type_list(self):

        filters = {"group__style__company__code": self.kwargs.get('company_code')}

        opt_filters = ["group"]

        for i in opt_filters:
            param = self.request.query_params.get('group')
            if param:
                filters[i] = param

        machine_types = MachineType.objects.filter(**filters)
        if machine_types.exists():
            return machine_types
        else:
            raise NotFound({'error': 'Типов оборудования не найдено'})

    def get_machine_type_entity(self):
        try:
            return MachineType.objects.get(group__style__company__code=self.kwargs.get('company_code'), pk=self.kwargs.get('pk'))
        except:
            raise NotFound({'error': 'Такого типа оборудования не найдено'})

    def create(self, request, *args, **kwargs):
        data = request.data
        
        self.check_name()

        try:
            serializer = MachineTypeApiSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return self.handler201
        except:
            return self.handler500

    def list(self, request, *args, **kwargs):
        
        machine_types = self.get_machine_type_list()
        
        try:
            serializer = MachineTypeApiSerializer(machine_types, many=True)
            data = serializer.data

            for i in range(1, len(data)+1):
                data[i-1].pop("group")
                data[i-1]["indent"] = i
                data[i-1]["count"] = MachineName.objects.filter(company__code=self.kwargs.get('company_code'), type__name=data[i-1]["name"]).count()

            return Response(data, status=200)
        except:
            return self.handler500

    def retrieve(self, request, *args, **kwargs):
        
        machine_type = self.get_machine_type_entity()

        try:
            serializer = MachineTypeApiSerializer(machine_type)
            return Response(serializer.data, status=200)
        except:
            return self.handler500

    def update(self, request, *args, **kwargs):
        
        machine_type = self.get_machine_type_entity()

        self.check_name()
        
        try:
            data = request.data
            serializer = MachineTypeApiSerializer(machine_type, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return self.handler200
        except:
            return self.handler500
    
    def destroy(self, request, *args, **kwargs):
        
        machine_type = self.get_machine_type_entity()
        
        try:
            machine_type.delete()
            return self.handler204
        except:
            return self.handler500
        