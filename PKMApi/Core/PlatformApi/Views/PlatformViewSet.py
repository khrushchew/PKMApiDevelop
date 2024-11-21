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

from rest_framework.decorators import permission_classes
from Core.UserApi.Permissions.permissions import IsInGroups
from rest_framework.permissions import IsAuthenticated


class PlatformApiViewSet(ViewSet):

    permission_classes = [IsAuthenticated]

    handler200 = Response(status=200)
    handler201 = Response(status=201)
    handler204 = Response(status=204)
    handler500 = Response({'detail': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    def get_platform_list(self):
        try:
            return Platform.objects.filter(company=self.request.user.company).order_by('indent')
        except:
            raise NotFound({'detail': 'Площадок не найдено'})
    
    def get_platform_entity(self):
        try:
            return Platform.objects.get(pk=self.kwargs.get('pk'))
        except:
            raise NotFound({'detail': 'Такой площадки не найдено'})

    def check_name(self):
        if Platform.objects.filter(name=self.request.data.get('name'), company=self.request.user.company).exists():
            raise ValidationError({'detail': 'Площадка с таким названием уже существует'})
    
    def check_indent(self):
        if Platform.objects.filter(indent=self.request.data.get('indent'), company=self.request.user.company).exists():
            raise ValidationError({'detail': 'Площадка с таким идентификатором уже существует'})

    company_code_param = openapi.Parameter(
        'company_code',
        openapi.IN_PATH,
        description="Код компании",
        type=openapi.TYPE_STRING,
        required=True
    )

    access_token_param = openapi.Parameter(
        'access',
        openapi.IN_HEADER,
        description='Токен доступа',
        type=openapi.TYPE_STRING,
        required=True,
        default='JWT {token}'
    )

    @swagger_auto_schema(
        tags=['platform - Площадка'],
        operation_summary ='Создание площадки',
        operation_description='Создаёт площадку для определённой компании',
        request_body=PlatformCreateApiSerializer,
        manual_parameters=[access_token_param],
        responses={
            201: "Успешное создание площадки",
            400: "Ошибка при обработке запроса",
            401: "Ошибка прав доступа",
            500: "Ошибка сервера"
        }
    )
    def create(self, request, *args, **kwargs):

        data = request.data

        data["company"] = request.user.company.pk

        self.check_name()
        self.check_indent()

        serializer = PlatformCreateApiSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
            return self.handler201
        except:
            return self.handler500
    
    @swagger_auto_schema(
        tags=['platform - Площадка'],
        operation_summary = 'Вывод списка площадок',
        operation_description= 'Выводит список площадок для определённой компании',
        manual_parameters=[access_token_param],
        responses={
            200: "Вывод всех найденных площадок",
            401: "Ошибка прав доступа",
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
        manual_parameters=[access_token_param],
        responses={
            200: "Вывод найденной площадок",
            401: "Ошибка прав доступа",
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
        manual_parameters=[access_token_param],
        request_body=PlatformUpdateApiSerializer,
        responses={
            200: "Успешное изменение",
            400: "Ошибка при обработке запроса",
            401: "Ошибка прав доступа",
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
        manual_parameters=[access_token_param],
        responses={
            200: "Успешное удаление",
            401: "Ошибка прав доступа",
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
    