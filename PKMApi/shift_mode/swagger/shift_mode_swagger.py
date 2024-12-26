from Core.swagger_params import ACCESS_TOKEN_PARAM
from drf_yasg.utils import swagger_auto_schema

from shift_mode.serializers.shift_mode_create_serializer import ShiftModeCreateSerializer
from shift_mode.serializers.shift_mode_list_serializer import ShiftModeListSerializer

from shift_mode.views.shift_mode_view import ShiftModeView


class ShiftModeSwaggerView(ShiftModeView):
    @swagger_auto_schema(
            tags=['shift_mode - Режимы сменности'],
            operation_summary='Создание режима сменности',
            operation_description='Создаёт режим сменности',
            manual_parameters=[ACCESS_TOKEN_PARAM],
            request_body=ShiftModeCreateSerializer,
            responses={
                201: 'Успешная обработка запроса',
                400: 'Ошибка при обработке запроса',
                500: 'Ошибка сервера'
            }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
            tags=['shift_mode - Режимы сменности'],
            operation_summary='Вывод списка режимов сменности',
            operation_description='Выводит список режимов сменности',
            manual_parameters=[ACCESS_TOKEN_PARAM],
            responses={
                200: ShiftModeListSerializer(many=True),
                400: 'Ошибка при обработке запроса',
                500: 'Ошибка сервера'
            }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
            tags=['shift_mode - Режимы сменности'],
            operation_summary='Изменнение режима сменности',
            operation_description='Изменяет режим сменности',
            manual_parameters=[ACCESS_TOKEN_PARAM],
            request_body=ShiftModeCreateSerializer,
            responses={
                200: 'Успешная обработка запроса',
                400: 'Ошибка при обработке запроса',
                500: 'Ошибка сервера'
            }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
            tags=['shift_mode - Режимы сменности'],
            operation_summary='Удаление режима сменности',
            operation_description='Удаляет режим сменности',
            manual_parameters=[ACCESS_TOKEN_PARAM],
            responses={
                200: 'Успешная обработка запроса',
                400: 'Ошибка при обработке запроса',
                500: 'Ошибка сервера'
            }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)