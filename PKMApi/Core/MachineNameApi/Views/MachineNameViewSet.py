from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from ..Serializers.MachineNameSerializer import MachineNameApiSerializer
from ..Serializers.MachineNameDetailSerializer import MachineNameDetailApiSerializer

from Core.models.MachineName import MachineName
from Core.models.Company import Company


class MachineNameApiViewSet(ViewSet):

    handler200 = Response(status=200)
    handler201 = Response(status=201)
    handler204 = Response(status=204)
    handler500 = Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)
    
    def get_company(self):
        try:
            return Company.objects.get(code=self.kwargs.get('company_code')).pk
        except:
            raise NotFound({'error': 'Такой компании не найдено'})
    
    def check_inv_number(self):
        if MachineName.objects.filter(company__code=self.kwargs.get('company_code'), inv_number=self.request.data.get('inv_number')).exists():
            raise ValidationError({'error': 'Такой инвентарный номер уже сущестует'})

    def get_machine_name_entity(self):
        try:
            return MachineName.objects.get(company__code=self.kwargs.get('company_code'), pk=self.kwargs.get('pk'))
        except:    
            raise NotFound({'error': 'Такое оборудование не найдено'})

    def get_machine_name_list(self):
            
        filters = {'company__code': self.kwargs.get('company_code')}
    
        optional_filters = ['area', 'type']
    
        for param in optional_filters:
            value = self.request.query_params.get(param)
            if value:
                filters[param] = value

        machine_names = MachineName.objects.filter(**filters)

        if machine_names.exists():
            return machine_names
        else:    
            raise NotFound({'error': 'Оборудования не найдено'})

    def create(self, request, *args, **kwargs):

        data = request.data
        data['company'] = self.get_company()

        self.check_inv_number()

        try:
            serializer = MachineNameApiSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return self.handler201
            else:
                return Response(serializer.errors, status=400)
        except:
            return self.handler500
    
    def retrieve(self, request, *args, **kwargs):

        machine_name = self.get_machine_name_entity()

        try:
            serializer = MachineNameApiSerializer(machine_name)
            return Response(serializer.data, status=200)
        except:
            return self.handler500
    
    def update(self, request, *args, **kwargs):

        machine_name = self.get_machine_name_entity()

        data = request.data
        data['company'] = self.get_company()

        self.check_inv_number()

        try:
            serializer = MachineNameApiSerializer(machine_name, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return self.handler200
        except:
            return self.handler500        

    def destroy(self, request, *args, **kwargs):

        machine_name = self.get_machine_name_entity()

        try:
            machine_name.delete()
            return self.handler204
        except:
            return self.handler500
    
    def list(self, request, *args, **kwargs):

        machine_names = self.get_machine_name_list()

        try:
            serializer = MachineNameDetailApiSerializer(machine_names, many=True)
            return Response(serializer.data, status=200)
        except:
            return self.handler500
