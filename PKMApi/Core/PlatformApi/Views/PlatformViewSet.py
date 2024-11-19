from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.viewsets import ViewSet

from ..Serializers.PlatformCreateSerializer import PlatformCreateApiSerializer
from ..Serializers.PlatformListSerializer import PlatformListApiSerializer
from ..Serializers.PlatformUpdateSerializer import PlatformUpdateApiSerializer

from Core.models.Company import Company
from Core.models.Platform import Platform


class PlatformApiViewSet(ViewSet):

    handler200 = Response(status=200)
    handler201 = Response(status=201)
    handler204 = Response(status=204)
    handler500 = Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    def get_company(self):
        company_code = self.kwargs.get('company_code')
        try:
            return Company.objects.get(code=company_code).pk
        except:
            raise NotFound({'error': 'Такой компании не найдено'})
    
    def get_platform_list(self):
        try:
            return Platform.objects.filter(company__code=self.kwargs.get('company_code'))
        except:
            raise NotFound({'error': 'Площадок не найдено'})
    
    def get_platform_entity(self):
        try:
            return Platform.objects.get(pk=self.kwargs.get('pk'))
        except:
            raise NotFound({'error': 'Такой площадки не найдено'})

    def check_name(self):
        if Platform.objects.filter(name=self.request.data.get('name'), company__code=self.kwargs.get('company_code')).exists():
            raise ValidationError({'error': 'Площадка с таким названием уже существует'})
    
    def check_indent(self):
        if Platform.objects.filter(indent=self.request.data.get('indent'), company__code=self.kwargs.get('company_code')).exists():
            raise ValidationError({'error': 'Площадка с таким идентификатором уже существует'})

    company_code_param = openapi.Parameter(
        'company_code',
        openapi.IN_PATH,
        description="Код компании",
        type=openapi.TYPE_STRING,
        required=True
    )


    @swagger_auto_schema(
        tags=['platform - Площадка'],
        operation_summary ='Создание площадки',
        operation_description='Создаёт площадку для определённой компании',
        manual_parameters=[company_code_param,],
        request_body=PlatformCreateApiSerializer,
        responses={
            201: "Успешное создание площадки",
            400: "Ошибка при обработке запроса",
            500: "Ошибка сервера"
        }
    )
    def create(self, request, *args, **kwargs):

        data = request.data

        data["company"] = self.get_company()

        self.check_name()
        self.check_indent()

        try:
            serializer = PlatformCreateApiSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return self.handler201
        except:
            return self.handler500
    
    @swagger_auto_schema(
        tags=['platform - Площадка'],
        operation_summary = 'Вывод списка площадок',
        operation_description= 'Выводит список площадок для определённой компании',
        manual_parameters=[company_code_param,],
        responses={
            200: "Вывод всех найденных площадок",
            404: "Ни одной площадки не найдено",
            500: "Ошибка сервера"
        }
    )
    def list(self, request, *args, **kwargs):

        platforms = self.get_platform_list()

        try:
            serializer = PlatformListApiSerializer(platforms, many=True)
            return Response(serializer.data, status=200)
        except:
            return self.handler500

    @swagger_auto_schema(
        tags=['platform - Площадка'],
        operation_summary = 'Вывод определённой площадки',
        operation_description= 'Выводит единственную площадку для определённой компании',
        manual_parameters=[company_code_param,],
        responses={
            200: "Вывод найденной площадок",
            404: "Площадки не найдено",
            500: "Ошибка сервера"
        }
    )
    def retrieve(self, request,  *args, **kwargs):
        platform = self.get_platform_entity()
        try:
            serializer = PlatformCreateApiSerializer(platform)
            return Response(serializer.data, status=200)
        except:
            return self.handler500
        
    @swagger_auto_schema(
        tags=['platform - Площадка'],
        operation_summary = 'Изменение определённой площадки',
        operation_description= 'Меняет определённую площадку для определённой компании',
        manual_parameters=[company_code_param,],
        request_body=PlatformUpdateApiSerializer,
        responses={
            200: "Успешное изменение",
            400: "Ошибка при обработке запроса",
            404: "Площадки не найдено",
            500: "Ошибка сервера"
        }
    )    
    def update(self, request, *args, **kwargs):

        data = request.data

        self.check_name()
        self.check_indent()

        platform = self.get_platform_entity()

        try:
            serializer = PlatformUpdateApiSerializer(platform, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(status=200)
            else:
                return Response(serializer.errors, status=400)
        except:
            return self.handler500

    @swagger_auto_schema(
        tags=['platform - Площадка'],
        operation_summary = 'Удаление определённой площадки',
        operation_description= 'Удаляет определённую площадку для определённой компании',
        manual_parameters=[company_code_param,],
        responses={
            200: "Успешное удаление",
            404: "Площадки не найдено",
            500: "Ошибка сервера"
        }
    )        
    def destroy(self, request, *args, **kwargs):
        platform = self.get_platform_entity()

        try:
            platform.delete()
            return Response(status=200)
        except:
            return self.handler500
    