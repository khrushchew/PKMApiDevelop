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
    
    @swagger_auto_schema(
            tags=['shift_working_day_mode - Режимы рабочего дня'],
            operation_summary='Вывод списка режимов рабочего дня',
            operation_description='Выводит список режимов рабочего дня',
            manual_parameters=[ACCESS_TOKEN_PARAM],
            responses={
                200: 'Успешная обработка запроса',
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
                200: 'Успешная обработка запроса',
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
    