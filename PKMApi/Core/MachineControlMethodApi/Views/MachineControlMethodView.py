from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import NotFound, ValidationError

from ..Serializers.MachineControlMethodSerializer import MachineControlMethodApiSerializer

from Core.models.MachineControlMethod import MachineControlMethod
from Core.models.Company import Company
from Core.models.MachineName import MachineName

class MachineControlMethodApiViewSet(ModelViewSet):

    serializer_class = MachineControlMethodApiSerializer

    handler200 = Response(status=200)
    handler500 = Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    def get_company(self):
        company_code = self.kwargs.get('company_code')
        try:
            return Company.objects.get(code=company_code)
        except:
            raise NotFound({'error': 'Такой компании не найдено'})
        
    def check_name(self):
        if MachineControlMethod.objects.filter(company__code=self.kwargs.get('company_code'), name=self.request.data.get('name')).exists():
            raise ValidationError({'error': 'Способ управления оборудованием с таким названием уже существует'})

    def get_machine_control_method_list(self):
        machine_control_methods = MachineControlMethod.objects.filter(company__code=self.kwargs.get('company_code'))
        if machine_control_methods.exists():
            return machine_control_methods
        else:
            raise NotFound({'error': 'Способов управления оборудованием не найдено'})

    def get_machine_control_method_entity(self):
        try:
            return MachineControlMethod.objects.get(company__code=self.kwargs.get('company_code'), pk=self.kwargs.get('pk'))
        except:
            raise NotFound({'error': 'Способа управления оборудованием не найдено'})

    def create(self, request, *args, **kwargs):
        data = request.data
        
        self.check_name()

        data["company"] = self.get_company().pk

        try:
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return self.handler200
        except:
            return self.handler500

    def list(self, request, *args, **kwargs):
        
        machine_control_methods = self.get_machine_control_method_list()
        
        try:
            serializer = self.get_serializer(machine_control_methods, many=True)
            data = serializer.data

            for i in range(1, len(data)+1):
                data[i-1].pop("company")
                data[i-1]["indent"] = i
                data[i-1]["count"] = MachineName.objects.filter(company__code=self.kwargs.get('company_code'), machine_control_method__name=data[i-1]["name"]).count()

            return Response(data, status=200)
        except:
            return self.handler500

    def retrieve(self, request, *args, **kwargs):
        
        machine_control_method = self.get_machine_control_method_entity()

        try:
            serializer = self.get_serializer(machine_control_method)
            return Response(serializer.data, status=200)
        except:
            return self.handler500

    def update(self, request, *args, **kwargs):
        
        machine_control_method = self.get_machine_control_method_entity()

        self.check_name()
        
        try:
            data = request.data
            data["company"] = self.get_company().pk
            serializer = self.get_serializer(machine_control_method, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return self.handler200
        except:
            return self.handler500
    
    def destroy(self, request, *args, **kwargs):
        
        machine_control_method = self.get_machine_control_method_entity()

        try:
            machine_control_method.delete()
            return self.handler200
        except:
            return self.handler500
        