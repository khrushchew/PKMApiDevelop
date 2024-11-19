from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError

from ..Serializers.SubdivisionCreateSerializer import SubdivisionCreateApiSerializer
from ..Serializers.SubdivisionListSerializer import SubdivisionListApiSerializer
from ..Serializers.SubdivisionRetrieveSerializer import SubdivisionRetrieveApiSerializer
from ..Serializers.SubdivisionUpdateSerializer import SubdivisionUpdateApiSerializer

from Core.models.Subdivision import Subdivision
from Core.models.Company import Company
from Core.models.User import User

class SubdivisionApiViewSet(ViewSet):
    def get_subdivision_list(self):
        company_code = self.kwargs.get('company_code')
        try:
            return Subdivision.objects.filter(company__code=company_code).order_by('name')
        except:
            raise NotFound({'error': 'Подразделений не найдено'})
    
    def get_subdivision_entity(self):
        pk = self.kwargs.get('pk')
        try:
            return Subdivision.objects.get(pk=pk)
        except:
            raise NotFound({'error': 'Такого подразделения не найдено'})

    def get_company(self):
        company_code = self.kwargs.get('company_code')
        try:
            return Company.objects.get(code=company_code)
        except:
            raise NotFound({'error': 'Такой компании не найдено'})

    def check_name(self):
        if Subdivision.objects.filter(name=self.request.data.get('name'), company__code=self.kwargs.get('company_code')).exists():
            raise ValidationError({'error': 'Подразделение с таким названием уже существует'})
        
    company_code_param = openapi.Parameter(
        'company_code',
        openapi.IN_PATH,
        description="Код компании",
        type=openapi.TYPE_STRING,
        required=True
    )

    @swagger_auto_schema(
        tags=['subdivision - Подразделение'],
        operation_summary='Создание подразделения',
        operation_description='Создаёт подразделение для определённой компании',
        manual_parameters=[company_code_param],
        request_body=SubdivisionCreateApiSerializer,
        responses={
            201: "Успешное создание подразделения",
            400: "Ошибка при обработке запроса",
            500: "Ошибка сервера",
        }
    )
    def create(self, request, *args, **kwargs):
        name = request.data.get('name')

        company = self.get_company()

        if Subdivision.objects.filter(name=name, company__code=company.code).exists():
            return Response({'error': 'Подразделение с таким названием уже существует'}, status=409)

        try:    
            Subdivision.objects.create(name=name, company=company)
            return Response(status=201)
        except:
            return Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)
        
    @swagger_auto_schema(
        tags=['subdivision - Подразделение'],
        operation_summary='Вывод списка подразделений',
        operation_description='Выводит список подразделений для определённой компании',
        manual_parameters=[company_code_param],
        responses={
            200: "Успешная обработка запроса",
            400: "Ошибка при обработке запроса",
            500: "Ошибка сервера",
        }
    )
    def list(self, request, *args, **kwargs):
        subdivisions = self.get_subdivision_list()

        try:
            serializer = SubdivisionListApiSerializer(subdivisions, many=True)

            if serializer.data:
                for i in range(1, len(serializer.data) + 1):
                    serializer.data[i - 1].setdefault("indent", i)

            data = serializer.data
            data.append({'indent': 0, 'name': 'Резерв', 'users': User.objects.filter(subdivision=None).count()})
        
            return Response(sorted(data, key=lambda i: i["indent"]), status=200)
        except:
            return Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)
    
    @swagger_auto_schema(
        tags=['subdivision - Подразделение'],
        operation_summary='Вывод определённого подразделения',
        operation_description='Выводит определённое подразделение для определённой компании',
        manual_parameters=[company_code_param],
        responses={
            200: "Успешная обработка запроса",
            400: "Ошибка при обработке запроса",
            500: "Ошибка сервера",
        }
    )
    def retrieve(self, request, *args, **kwargs):
        subdivision = self.get_subdivision_entity()

        try:
            serializer = SubdivisionRetrieveApiSerializer(subdivision)
            return Response(serializer.data, status=200)
        except:
            return Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)
        
    @swagger_auto_schema(
        tags=['subdivision - Подразделение'],
        operation_summary='Изменение определённого подразделения',
        operation_description='Изменяет определённое подразделение для определённой компании',
        manual_parameters=[company_code_param],
        responses={
            200: "Успешная обработка запроса",
            400: "Ошибка при обработке запроса",
            500: "Ошибка сервера",
        }
    )
    def update(self, request, *args, **kwargs):
        
        subdivision = self.get_subdivision_entity()

        self.check_name()

        serializer = SubdivisionUpdateApiSerializer(subdivision, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        try:
            serializer.save()
            return Response(status=200)
        except:
            return Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)
        
    @swagger_auto_schema(
        tags=['subdivision - Подразделение'],
        operation_summary='Удаление определённого подразделения',
        operation_description='Удаляет определённое подразделение для определённой компании',
        manual_parameters=[company_code_param],
        responses={
            200: "Успешная обработка запроса",
            400: "Ошибка при обработке запроса",
            500: "Ошибка сервера",
        }
    )
    def destroy(self, request, *args, **kwargs):
        subdivision = self.get_subdivision_entity()

        try:
            subdivision.delete()
            return Response(status=200)
        except:
            return Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)
        