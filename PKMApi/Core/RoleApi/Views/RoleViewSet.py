from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from ..Serializers.RoleSerializer import RoleApiSerializer

from Core.models.Role import Role
from Core.models.Company import Company


class RoleApiViewSet(ModelViewSet):
    serializer_class = RoleApiSerializer

    def get_role_list(self):
        company_code = self.kwargs.get('company_code')
        try:
            return Role.objects.filter(company__code=company_code)
        except:
            raise NotFound({'error': 'Ролей не найдено'})
    
    def get_role_entity(self):
        pk = self.kwargs.get('pk')
        try:
            return Role.objects.get(pk=pk)
        except:
            raise NotFound({'error': 'Такой роли не найдено'})

    def get_company(self):
        company_code = self.kwargs.get('company_code')
        try:
            return Company.objects.get(code=company_code)
        except:
            raise NotFound({'error': 'Такой компании не найдено'})

    
    def create(self, request, *args, **kwargs):
        name = request.data.get('name')

        company = self.get_company()

        if Role.objects.filter(name=name, company__code=company.code).exists():
            return Response({'error': 'Роль с таким названием уже существует'}, status=409)

        try:    
            Role.objects.create(name=name, company=company)
            return Response(status=200)
        except:
            return Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    def list(self, request, *args, **kwargs):
        roles = self.get_role_list()

        try:
            serializer = self.get_serializer(roles, many=True)

            for i in range(1, len(serializer.data) + 1):
                serializer.data[i - 1].setdefault("id", i)

            return Response(serializer.data, status=200)
        except:
            return Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)
    
    def retrieve(self, request, *args, **kwargs):
        role = self.get_role_entity()

        try:
            serializer = self.get_serializer(role)
            return Response(serializer.data, status=200)
        except:
            return Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    def update(self, request, *args, **kwargs):
        name = request.data.get('name')

        role = self.get_role_entity()
       
        if Role.objects.filter(name=name, company__code=role.company.code).exists():
            return Response({'error': 'Роль с таким названием уже существует'}, status=409)

        try:
            role.name = name
            role.save()
            return Response(status=200)
        except:
            return Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)
        

    def destroy(self, request, *args, **kwargs):
        
        role = self.get_role_entity()

        try:
            role.delete()
            return Response(status=200)
        except:
            return Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)
        