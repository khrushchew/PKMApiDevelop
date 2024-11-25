from area.serializers.area_create_serializer import AreaCreateSerializer
from area.views.area_view import AreaView
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class AreaSwaggerView(AreaView):
    ACCESS_TOKEN_PARAM = openapi.Parameter(
        'access_token',
        openapi.IN_HEADER,
        description='Токен доступа',
        type=openapi.TYPE_STRING,
        required=True,
        default='JWT {token}'
    )

    @swagger_auto_schema(
        tags=['area - Участок'],
        operation_summary='Добавление участка',
        operation_description='Добавляет определённый участок',
        request_body=AreaCreateSerializer,
        manual_parameters=[ACCESS_TOKEN_PARAM],
        responses={
            201: 'Успешное создание',
            400: 'Ошибка при создании',
            500: 'Ошибка сервера'
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        tags=['area - Участок'],
        operation_summary='Вывод списка участков',
        operation_description='Выводит список участков',
        manual_parameters=[ACCESS_TOKEN_PARAM],
        responses={
            200: 'Успешный вывод списка участков',
            500: 'Ошибка сервера'
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        tags=['area - Участок'],
        operation_summary='Вывод определённого участка',
        operation_description='Выводит определённый участок',
        manual_parameters=[ACCESS_TOKEN_PARAM],
        responses={
            200: 'Успешный вывод определённого участка',
            500: 'Ошибка сервера'
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        tags=['area - Участок'],
        operation_summary='Изменение участка',
        operation_description='Изменяет определённый участок',
        request_body=AreaCreateSerializer,
        manual_parameters=[ACCESS_TOKEN_PARAM],
        responses={
            200: 'Успешное изменение',
            400: 'Ошибка при изменении',
            500: 'Ошибка сервера'
        }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['area - Участок'],
        operation_summary='Удаление участка',
        operation_description='Удаляет определённый участок',
        manual_parameters=[ACCESS_TOKEN_PARAM],
        responses={
            200: 'Успешное удаление',
            500: 'Ошибка сервера'
        }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
