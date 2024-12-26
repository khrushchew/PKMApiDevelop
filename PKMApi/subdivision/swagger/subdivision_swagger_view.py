from drf_yasg.utils import swagger_auto_schema

from Core.swagger_params import ACCESS_TOKEN_PARAM

from subdivision.serializers.subdivision_create_serializer import SubdivisionCreateSerializer
from subdivision.serializers.subdivision_list_serializer import SubdivisionListSerializer
from subdivision.serializers.subdivision_retrieve_serializer import SubdivisionRetrieveSerializer
from subdivision.serializers.subdivision_update_serializer import SubdivisionUpdateSerializer

from subdivision.views.subdivision_view import SubdivisionView


class SubdivisionSwaggerView(SubdivisionView):
    @swagger_auto_schema(
        tags=['subdivision - Подразделение'],
        operation_summary='Создание подразделения',
        operation_description='Создаёт подразделение для определённой компании',
        manual_parameters=[ACCESS_TOKEN_PARAM],
        request_body=SubdivisionCreateSerializer,
        responses={
            201: "Успешное создание подразделения",
            400: "Ошибка при обработке запроса",
            500: "Ошибка сервера",
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
        
    @swagger_auto_schema(
        tags=['subdivision - Подразделение'],
        operation_summary='Вывод списка подразделений',
        operation_description='Выводит список подразделений для определённой компании',
        manual_parameters=[ACCESS_TOKEN_PARAM],
        responses={
            200: SubdivisionListSerializer(many=True),
            400: "Ошибка при обработке запроса",
            500: "Ошибка сервера",
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    
    @swagger_auto_schema(
        tags=['subdivision - Подразделение'],
        operation_summary='Вывод определённого подразделения',
        operation_description='Выводит определённое подразделение для определённой компании',
        manual_parameters=[ACCESS_TOKEN_PARAM],
        responses={
            200: SubdivisionRetrieveSerializer,
            400: "Ошибка при обработке запроса",
            500: "Ошибка сервера",
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

        
    @swagger_auto_schema(
        tags=['subdivision - Подразделение'],
        operation_summary='Изменение определённого подразделения',
        operation_description='Изменяет определённое подразделение для определённой компании',
        manual_parameters=[ACCESS_TOKEN_PARAM],
        request_body=SubdivisionUpdateSerializer,
        responses={
            200: "Успешная обработка запроса",
            400: "Ошибка при обработке запроса",
            500: "Ошибка сервера",
        }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

        
    @swagger_auto_schema(
        tags=['subdivision - Подразделение'],
        operation_summary='Удаление определённого подразделения',
        operation_description='Удаляет определённое подразделение для определённой компании',
        manual_parameters=[ACCESS_TOKEN_PARAM],
        responses={
            200: "Успешная обработка запроса",
            400: "Ошибка при обработке запроса",
            500: "Ошибка сервера",
        }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
        
        