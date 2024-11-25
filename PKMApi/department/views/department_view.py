from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.viewsets import ViewSet

from ..serializers.department_create_serializer import DepartmentCreateSerializer
from ..serializers.department_list_serializer import DepartmentListSerializer
from ..serializers.department_retrieve_serializer import DepartmentRetrieveSerializer

from Core.models.Department import Department
from Core.models.Platform import Platform


class DepartmentView(ViewSet):

    permission_classes = [IsAuthenticated]

    handler200 = Response(status=200)
    handler500 = Response({'detail': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    def get_platform(self, request):
        platform_pk = request.data.get('platform_pk')
        try:
            return Platform.objects.get(pk=platform_pk)
        except:
            raise NotFound({'detail': 'Такой площадки не найдено'})

    def get_department_list(self):

        filters = {"platform__company": self.request.user.company}

        opt_filters = ["platform"]

        for i in opt_filters:
            param = self.request.query_params.get('platform')
            if param:
                filters[i] = param
        departments = Department.objects.filter(**filters).order_by('indent')
        if departments.exists():
            return departments
        else:
            raise NotFound({'detail': 'Цехов не найдено'})
        
    def get_department_entity(self):
        try:
            return Department.objects.get(pk=self.kwargs.get('pk'))
        except:
            raise NotFound({'detail': 'Такого цеха не найдено'})
    
    def check_indent(self):
        if Department.objects.filter(indent=self.request.data.get('indent'), platform__company=self.request.user.company).exists():
            raise ValidationError({'detail': 'Цех с таким идентификатором уже существует'})
    
    def check_name(self):
        if Department.objects.filter(name=self.request.data.get('name'), platform__company=self.request.user.company).exists():
            raise ValidationError({'detail': 'Цех с таким названием уже существует'})

    def create(self, request, *args, **kwargs):

        data = request.data

        self.check_indent()
        self.check_name()
        
        serializer = DepartmentCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return self.handler200

    def list(self, request, *args, **kwargs):
        departments = self.get_department_list()
        try:
            serializer = DepartmentListSerializer(departments, many=True)
            return Response(serializer.data, status=200)
        except:
            return self.handler500
    
    def retrieve(self, request, *args, **kwargs):
        department = self.get_department_entity()
        try:
            serializer = DepartmentRetrieveSerializer(department)
            return Response(serializer.data, status=200)
        except:
            return self.handler500

    def update(self, request, *args, **kwargs):
        
        data = request.data
        
        department = self.get_department_entity()

        serializer = DepartmentRetrieveSerializer(department, data=data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return self.handler200

    def destroy(self, request, *args, **kwargs):
        department = self.get_department_entity()
        try:
            department.delete()
            return self.handler200
        except:
            return self.handler500
        