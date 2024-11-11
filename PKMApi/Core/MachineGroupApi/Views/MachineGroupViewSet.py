from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.exceptions import NotFound, ValidationError

from ..Serializers.MachineGroupSerializer import MachineGroupApiSerializer

from Core.models.MachineStyle import MachineStyle

from Core.models.MachineGroup import MachineGroup
from Core.models.MachineName import MachineName

class MachineGroupApiViewSet(ViewSet):

    handler200 = Response(status=200)
    handler201 = Response(status=201)
    handler204 = Response(status=204)
    handler500 = Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    def check_name(self):
        if MachineGroup.objects.filter(style__company__code=self.kwargs.get('company_code'), style=self.request.data.get('style'), name=self.request.data.get('name')).exists():
            raise ValidationError({'error': 'Группа оборудования с таким названием уже существует'})

    def get_machine_group_list(self):

        filters = {"style__company__code": self.kwargs.get('company_code')}

        opt_filters = ["style"]

        for i in opt_filters:
            param = self.request.query_params.get('style')
            if param:
                filters[i] = param

        machine_groups = MachineGroup.objects.filter(**filters)
        if machine_groups.exists():
            return machine_groups
        else:
            raise NotFound({'error': 'Групп оборудования не найдено'})

    def get_machine_group_entity(self):
        try:
            return MachineGroup.objects.get(style__company__code=self.kwargs.get('company_code'), pk=self.kwargs.get('pk'))
        except:
            raise NotFound({'error': 'Такого вида оборудования не найдено'})

    def create(self, request, *args, **kwargs):
        data = request.data
        
        self.check_name()

        try:
            serializer = MachineGroupApiSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return self.handler201
        except:
            return self.handler500

    def list(self, request, *args, **kwargs):
        
        machine_groups = self.get_machine_group_list()
        
        try:
            serializer = MachineGroupApiSerializer(machine_groups, many=True)
            data = serializer.data

            for i in range(1, len(data)+1):
                data[i-1].pop("style")
                data[i-1]["indent"] = i
                data[i-1]["count"] = MachineName.objects.filter(company__code=self.kwargs.get('company_code'), type__group__name=data[i-1]["name"]).count()

            return Response(data, status=200)
        except:
            return self.handler500

    def retrieve(self, request, *args, **kwargs):
        
        machine_group = self.get_machine_group_entity()

        try:
            serializer = MachineGroupApiSerializer(machine_group)
            return Response(serializer.data, status=200)
        except:
            return self.handler500

    def update(self, request, *args, **kwargs):
        
        machine_group = self.get_machine_group_entity()

        self.check_name()
        
        try:
            data = request.data
            serializer = MachineGroupApiSerializer(machine_group, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return self.handler200
        except:
            return self.handler500
    
    def destroy(self, request, *args, **kwargs):
        
        machine_group = self.get_machine_group_entity()

        try:
            machine_group.delete()
            return self.handler204
        except:
            return self.handler500
        