from Core.swagger_params import ACCESS_TOKEN_PARAM
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.permissions import IsAuthenticated

from datetime import datetime, timedelta

from shift_working_day_mode.serializers.shift_working_day_mode_create_serializer import ShiftWorkingDayModeCreateSerializer
from shift_working_day_mode.serializers.shift_working_day_mode_update_serializer import ShiftWorkingDayModeUpdateSerializer
from shift_working_day_mode.serializers.shift_working_day_mode_list_serializer import ShiftWorkingDayModeListSerializer
from shift_working_day_mode.serializers.shift_working_day_mode_retrieve_serializer import ShiftWorkingDayModeRetrieveSerializer

from shift_working_day_mode.views.shift_working_day_mode_view import ShiftWorkingDayModeView


class ShiftWorkingDayModeSwaggerView(ShiftWorkingDayModeView):
    @swagger_auto_schema(
            tags=['shift_working_day_mode - Режимы рабочего дня'],
            operation_summary='Создание режима рабочего дня',
            operation_description='Создаёт режим рабочего дня',
            manual_parameters=[ACCESS_TOKEN_PARAM],
            request_body=ShiftWorkingDayModeCreateSerializer,
            responses={
                200: 'Успешная обработка запроса',
                400: 'Ошибка при обработке запроса',
                500: 'Ошибка сервера'
            }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    from drf_yasg import openapi

    @swagger_auto_schema(
    tags=['shift_working_day_mode - Режимы рабочего дня'],
    operation_summary='Вывод списка режимов рабочего дня',
    operation_description='Выводит список режимов рабочего дня',
    manual_parameters=[ACCESS_TOKEN_PARAM],
    responses={
        200: openapi.Response(
            description="Список режимов рабочего дня",
            schema=openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'pk': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'code': openapi.Schema(type=openapi.TYPE_STRING),
                        'name': openapi.Schema(type=openapi.TYPE_STRING),
                        'start_time': openapi.Schema(type=openapi.TYPE_STRING),
                        'end_time': openapi.Schema(type=openapi.TYPE_STRING),
                        'start_pause_1': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                        'end_pause_1': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                        'start_pause_2': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                        'end_pause_2': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                        'start_pause_3': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                        'end_pause_3': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                        'start_pause_4': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                        'end_pause_4': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                        'start_pause_5': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                        'end_pause_5': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                        'start_pause_6': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                        'end_pause_6': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                        'start_pause_7': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                        'end_pause_7': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                        'start_pause_8': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                        'end_pause_8': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                        'start_pause_9': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                        'end_pause_9': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                        'start_pause_10': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                        'end_pause_10': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                    }
                )
            )
        ),
        400: 'Ошибка при обработке запроса',
        500: 'Ошибка сервера'
    }
)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
            tags=['shift_working_day_mode - Режимы рабочего дня'],
            operation_summary='Вывод режима рабочего дня',
            operation_description='Выводит режим рабочего дня',
            manual_parameters=[ACCESS_TOKEN_PARAM],
            responses={
                200: ShiftWorkingDayModeRetrieveSerializer,
                400: 'Ошибка при обработке запроса',
                500: 'Ошибка сервера'
            }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
            tags=['shift_working_day_mode - Режимы рабочего дня'],
            operation_summary='Изменение режима рабочего дня',
            operation_description='Изменяет режим рабочего дня',
            manual_parameters=[ACCESS_TOKEN_PARAM],
            request_body=ShiftWorkingDayModeUpdateSerializer,
            responses={
                200: 'Успешная обработка запроса',
                400: 'Ошибка при обработке запроса',
                500: 'Ошибка сервера'
            }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
            tags=['shift_working_day_mode - Режимы рабочего дня'],
            operation_summary='Удаление режима рабочего дня',
            operation_description='Удаляет режим рабочего дня',
            manual_parameters=[ACCESS_TOKEN_PARAM],
            responses={
                200: 'Успешная обработка запроса',
                400: 'Ошибка при обработке запроса',
                500: 'Ошибка сервера'
            }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    