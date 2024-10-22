from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.viewsets import ModelViewSet

from ..Serializers.DepartmentSerializer import DepartmentApiSerializer

from Core.models.Department import Department
from Core.models.Platform import Platform


class DepartmentApiViewSet(ModelViewSet):

    handler200 = Response(status=200)
    handler500 = Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    serializer_class = DepartmentApiSerializer

    def get_platform(self, request):
        platform_pk = request.data.get('platform_pk')
        try:
            return Platform.objects.get(pk=platform_pk)
        except:
            raise NotFound({'error': 'Такой площадки не найдено'})

    def get_department_list(self):
        company_code = self.kwargs.get('company_code')
        try:
            return Department.objects.filter(platform__company__code=company_code)
        except:
            raise NotFound({'error': 'Цехов не найдено'})
        
    def get_department_entity(self):
        pk = self.kwargs.get('pk')
        try:
            return Department.objects.get(pk=pk)
        except:
            raise NotFound({'error': 'Такого цеха не найдено'})
    
    def create(self, request, *args, **kwargs):

        indent = request.data.get('indent')
        name = request.data.get('name')
        main_user = request.data.get('main_user')

        platform = self.get_platfrom()

        if Department.objects.filter(indent=indent, platform__company__code=platform.company.code).exists():
            raise ValidationError({'error': 'Цех с таким идентификатором уже существует'})
        
        if Department.objects.filter(name=name, platform__company__code=platform.company.code).exists():
            raise ValidationError({'error': 'Цех с таким названием уже существует'})
        
        try:
            Department.objects.create(indent=indent, name=name, main_user=main_user, platform=platform)
            return self.handler200
        except:
            return self.handler500
    
    def list(self, request, *args, **kwargs):
        departments = self.get_department_list()
        try:
            serializer = self.get_serializer(departments, many=True)
            return Response(serializer.data, status=200)
        except:
            return self.handler500
    
    def retrieve(self, request, *args, **kwargs):
        department = self.get_department_entity()
        try:
            serializer = self.get_serializer(department)
            return Response(serializer.data, status=200)
        except:
            return self.handler500

    def partial_update(self, request, *args, **kwargs):
        indent = request.data.get('indent')
        name = request.data.get('name')
        main_user = request.data.get('main_user')

        department = self.get_department_entity()

        try:
            if indent:
                department.indent = indent
            if name:
                department.name = name
            if main_user:
                department.main_user = main_user
            if request.data.get('platform_pk'):
                platform = self.get_platform()
                department.platform = platform
            department.save()
            return self.handler200
        except:
            return self.handler500
    
    def destroy(self, request, *args, **kwargs):
        department = self.get_department_entity()
        try:
            department.delete()
            return self.handler200
        except:
            return self.handler500
        