from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from ..Serializers.MachineNameSerializer import MachineNameApiSerializer

from Core.models.MachineName import MachineName
from Core.models.Company import Company

class MachineNameApiViewSet(ModelViewSet):
    serializer_class = MachineNameApiSerializer
    handler200 = Response(status=200)
    handler500 = Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)
    
    def get_company(self):
        try:
            return Company.objects.get(code=self.kwargs.get('company'))
        except:
            raise NotFound({'error': 'Такой компании не найдено'})
        
    def create(self, request, *args, **kwargs):

        company = self.get_company()

        data = request.data
        print(data)
        data["company"] = company.pk

        serializer = self.get_serializer(data)
        print(serializer)