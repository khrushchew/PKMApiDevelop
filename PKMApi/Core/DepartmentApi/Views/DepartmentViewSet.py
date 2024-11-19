from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.viewsets import ViewSet

from ..Serializers.DepartmentCreateSerializer import DepartmentCreateApiSerializer
from ..Serializers.DepartmentListSerializer import DepartmentListApiSerializer
from ..Serializers.DepartmentRetrieveApiSerializer import DepartmentRetrieveApiSerializer

from Core.models.Department import Department
from Core.models.Platform import Platform


class DepartmentApiViewSet(ViewSet):

    handler200 = Response(status=200)
    handler500 = Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    def get_platform(self, request):
        platform_pk = request.data.get('platform_pk')
        try:
            return Platform.objects.get(pk=platform_pk)
        except:
            raise NotFound({'error': 'Такой площадки не найдено'})

    def get_department_list(self):

        filters = {"platform__company__code": self.kwargs.get('company_code')}

        opt_filters = ["platform"]

        for i in opt_filters:
            param = self.request.query_params.get('platform')
            if param:
                filters[i] = param
        departments = Department.objects.filter(**filters).order_by('indent')
        if departments.exists():
            return departments
        else:
            raise NotFound({'error': 'Цехов не найдено'})
        
    def get_department_entity(self):
        id = self.kwargs.get('id')
        try:
            return Department.objects.get(id=id)
        except:
            raise NotFound({'error': 'Такого цеха не найдено'})
    
    def check_indent(self):
        if Department.objects.filter(indent=self.request.data.get('indent'), platform__company__code=self.kwargs.get('company_code')).exists():
            raise ValidationError({'error': 'Цех с таким идентификатором уже существует'})
    
    def check_name(self):
        if Department.objects.filter(name=self.request.data.get('name'), platform__company__code=self.kwargs.get('company_code')).exists():
            raise ValidationError({'error': 'Цех с таким названием уже существует'})

    company_code_param = openapi.Parameter(
        'company_code',
        openapi.IN_PATH,
        description="Код компании",
        type=openapi.TYPE_STRING,
        required=True
    )

    @swagger_auto_schema(
        tags=['department - Цех'],
        operation_summary='Создание цеха',
        operation_description='Создаёт цех для определённой компании',
        manual_parameters=[company_code_param],
        request_body=DepartmentCreateApiSerializer,
        responses={
            201: "Успешное создание цеха",
            400: "Ошибка при обработке запроса",
        }
    )
    def create(self, request, *args, **kwargs):

        data = request.data

        self.check_indent()
        self.check_name()
        
        serializer = DepartmentCreateApiSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return self.handler200

    @swagger_auto_schema(
        tags=['department - Цех'],
        operation_summary='Вывод списка цехов',
        operation_description='Выводит список цехов для определённой компании',
        manual_parameters=[company_code_param],
        responses={
            200: "Вывод всех найденных цехов",
            400: "Ошибка при обработке запроса",
            404: "Не найдено ни одного цеха",
            500: "Ошибка сервера"
        }
    )
    def list(self, request, *args, **kwargs):
        departments = self.get_department_list()
        try:
            serializer = DepartmentListApiSerializer(departments, many=True)
            return Response(serializer.data, status=200)
        except:
            return self.handler500
    
    @swagger_auto_schema(
        tags=['department - Цех'],
        operation_summary='Вывод определённого цеха',
        operation_description='Выводит определённый цех для определённой компании',
        manual_parameters=[company_code_param],
        responses={
            200: "Вывод найденного цехов",
            400: "Ошибка при обработке запроса",
            404: "Не найдено такого цеха",
            500: "Ошибка сервера"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        department = self.get_department_entity()
        try:
            serializer = DepartmentRetrieveApiSerializer(department)
            return Response(serializer.data, status=200)
        except:
            return self.handler500

    @swagger_auto_schema(
        tags=['department - Цех'],
        operation_summary='Изменения определённого цеха',
        operation_description='Изменяет определённый цех для определённой компании',
        manual_parameters=[company_code_param],
        responses={
            200: "Успешное изменение цеха",
            400: "Ошибка при обработке запроса",
            404: "Не найдено такого цеха",
            500: "Ошибка сервера"
        }
    )
    def update(self, request, *args, **kwargs):
        
        data = request.data
        
        department = self.get_department_entity()

        serializer = DepartmentRetrieveApiSerializer(department, data=data, partial=True)

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
        