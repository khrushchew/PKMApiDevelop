from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated

from machine_style.serializers.machine_style_create_serializer import MachineStyleCreateSerializer
from machine_style.serializers.machine_style_list_serializer import MachineStyleListSerializer
from machine_style.serializers.machine_style_retrieve_serializer import MachineStyleRetrieveSerializer
from machine_style.serializers.machine_style_update_serializer import MachineStyleUpdateSerializer

from Core.models.MachineStyle import MachineStyle
from Core.models.MachineName import MachineName


class MachineStyleView(ViewSet):

    permission_classes = [IsAuthenticated]

    handler200 = Response(status=200)
    handler201 = Response({'detail': 'Вид оборудования успешно создан'}, status=201)
    handler500 = Response({'detail': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    def get_machine_style_list(self):
        machine_styles = MachineStyle.objects.filter(company=self.request.user.company)
        if machine_styles.exists():
            return machine_styles
        else:
            raise NotFound({'detail': 'Видов оборудования не найдено'})

    def get_machine_style_entity(self):
        try:
            return MachineStyle.objects.get(company=self.request.user.company, pk=self.kwargs.get('pk'))
        except:
            raise NotFound({'detail': 'Такого вида оборудования не найдено'})

    def create(self, request, *args, **kwargs):
        data = request.data
        data['company'] = request.user.company.id
        
        serializer = MachineStyleCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        try:
            serializer.save()
            return self.handler201
        except:
            return self.handler500

    def list(self, request, *args, **kwargs):
        
        machine_styles = self.get_machine_style_list()
        
        try:
            serializer = MachineStyleListSerializer(machine_styles, many=True)
            
            data = serializer.data

            for i in range(1, len(data)+1):
                data[i-1]["indent"] = i
            res = [{"indent": 0, "name": "Резерв", "count": MachineName.objects.filter(company=request.user.company, type=None).count()}]
            res.extend(data)

            return Response(res, status=200)
        except:
            return self.handler500
    
    def retrieve(self, request, *args, **kwargs):
        
        machine_style = self.get_machine_style_entity()
        serializer = MachineStyleRetrieveSerializer(machine_style)
        try:
            return Response(serializer.data, status=200)
        except:
            return self.handler500

    def update(self, request, *args, **kwargs):

        machine_style = self.get_machine_style_entity()

        serializer = MachineStyleUpdateSerializer(machine_style, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        try:    
            serializer.save()
            return self.handler200
        except:
            return self.handler500
    
    def destroy(self, request, *args, **kwargs):
        
        machine_style = self.get_machine_style_entity()

        try:
            machine_style.delete()
            return self.handler200
        except:
            return self.handler500
        