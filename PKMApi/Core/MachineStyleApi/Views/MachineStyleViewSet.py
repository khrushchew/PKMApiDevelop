from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import NotFound, ValidationError

from ..Serializers.MachineStyleSerializer import MachineStyleApiSerializer

from Core.models.Company import Company
from Core.models.MachineStyle import MachineStyle

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
        
        machine_styles = MachineStyle.objects.filter(company=self.get_company())

        try:
            serializer = self.get_serializer(machine_styles, many=True)
            return Response(serializer.data, status=200)
        except:
            return self.handler500

    

