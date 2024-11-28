from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.exceptions import NotFound, ValidationError

from machine_group.serializer.machine_group_create_serializer import MachineGroupCreateSerializer
from machine_group.serializer.machine_group_list_serializer import MachineGroupListSerializer
from machine_group.serializer.machine_group_retrieve_serializer import MachineGroupRetrieveSerializer
from machine_group.serializer.machine_group_update_serializer import MachineGroupUpdateSerializer

from Core.models.MachineStyle import MachineStyle

from Core.models.MachineGroup import MachineGroup
from Core.models.MachineName import MachineName

class MachineGroupView(ViewSet):

    handler200 = Response(status=200)
    handler201 = Response({'detail': 'Группа оборудования успешно создана'}, status=201)
    handler500 = Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    def get_machine_group_list(self):

        filters = {"style__company": self.request.user.company}

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
            return MachineGroup.objects.get(style__company=self.request.user.company, pk=self.kwargs.get('pk'))
        except:
            raise NotFound({'error': 'Такого вида оборудования не найдено'})

    def create(self, request, *args, **kwargs):
        data = request.data
        
        serializer = MachineGroupCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        try:    

            serializer.save()
            return self.handler201
        except:
            return self.handler500

    def list(self, request, *args, **kwargs):
        
        machine_groups = self.get_machine_group_list()
        
        serializer = MachineGroupListSerializer(machine_groups, many=True)
        data = serializer.data
        
        for i in range(1, len(data)+1):
            data[i-1]["indent"] = i
            
        try:
            return Response(data, status=200)
        except:
            return self.handler500

    def retrieve(self, request, *args, **kwargs):
        
        machine_group = self.get_machine_group_entity()

        serializer = MachineGroupRetrieveSerializer(machine_group)

        try:
            return Response(serializer.data, status=200)
        except:
            return self.handler500

    def update(self, request, *args, **kwargs):
        
        machine_group = self.get_machine_group_entity()

        data = request.data
        serializer = MachineGroupUpdateSerializer(machine_group, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        try:    
            serializer.save()
            return self.handler200
        except:
            return self.handler500
    
    def destroy(self, request, *args, **kwargs):
        
        machine_group = self.get_machine_group_entity()

        try:
            machine_group.delete()
            return self.handler200
        except:
            return self.handler500
        