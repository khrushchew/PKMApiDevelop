from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.viewsets import ModelViewSet

from ..Serializers.UserSerializer import UserApiSerializer

from Core.models.User import User
from Core.models.Company import Company

class UserApiVewSet(ModelViewSet):

    serializer_class = UserApiSerializer

    handler200 = Response(status=200)
    handler500 = Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    def get_company(self):
        try:
            return Company.objects.get(pk=self.kwargs.get('company'))
        except:
            return NotFound({'error': 'Такой компании не найдено'})
        
    def create(self, request, *args, **kwargs):
        
        data = request.data

        company = self.get_company

        