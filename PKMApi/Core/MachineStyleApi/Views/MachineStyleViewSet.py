from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import NotFound, ValidationError

from ..Serializers.MachineStyleSerializer import MachineStyleApiSerializer

from Core.models.Company import Company
from Core.models.MachineStyle import MachineStyle
from Core.models.MachineName import MachineName

class MachineStyleApiViewSet(ModelViewSet):

    serializer_class = MachineStyleApiSerializer

    handler200 = Response(status=200)
    handler500 = Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    def get_company(self):
        company_code = self.kwargs.get('company_code')
        try:
            return Company.objects.get(code=company_code)
        except:
            raise NotFound({'error': 'Такой компании не найдено'})
        
    def check_name(self):
        if MachineStyle.objects.filter(company__code=self.kwargs.get('company_code'), name=self.request.data.get('name')).exists():
            raise ValidationError({'error': 'Вид оборудования с таким названием уже существует'})

    def get_machine_style_list(self):
        machine_styles = MachineStyle.objects.filter(company__code=self.kwargs.get('company_code'))
        if machine_styles.exists():
            return machine_styles
        else:
            raise NotFound({'error': 'Видов оборудования не найдено'})

    def get_machine_style_entity(self):
        try:
            return MachineStyle.objects.get(company__code=self.kwargs.get('company_code'), pk=self.kwargs.get('pk'))
        except:
            raise NotFound({'error': 'Такого вида оборудования не найдено'})

    def create(self, request, *args, **kwargs):
        data = request.data
        
        self.check_name()

        data['company'] = str(self.get_company().pk) 

        try:
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return self.handler200
        except:
            return self.handler500

    def list(self, request, *args, **kwargs):
        
        machine_styles = self.get_machine_style_list()
        
        try:
            serializer = self.get_serializer(machine_styles, many=True)
            data = serializer.data

            for i in range(1, len(data)+1):
                data[i-1].pop("company")
                data[i-1]["indent"] = i
                data[i-1]["count"] = MachineName.objects.filter(company__code=self.kwargs.get('company_code'), type__group__style__name=data[i-1]["name"]).count()

            res = [{"indent": 0, "name": "Резерв", "count": MachineName.objects.filter(company__code=self.kwargs.get('company_code'), type=None).count()}]
            res.extend(data)
            return Response(res, status=200)
        except:
            return self.handler500

    def retrieve(self, request, *args, **kwargs):
        
        machine_style = self.get_machine_style_entity()

        try:
            serializer = self.get_serializer(machine_style)
            return Response(serializer.data, status=200)
        except:
            return self.handler500

    def update(self, request, *args, **kwargs):

        machine_style = self.get_machine_style_entity()

        self.check_name()

        try:
            serializer = self.get_serializer(machine_style, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
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
        