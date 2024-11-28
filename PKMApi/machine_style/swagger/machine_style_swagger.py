from Core.swagger_params import ACCESS_TOKEN_PARAM

from drf_yasg.utils import swagger_auto_schema

from machine_style.views.machine_style_view import MachineStyleView

from machine_style.serializers.machine_style_create_serializer import MachineStyleCreateSerializer
from machine_style.serializers.machine_style_update_serializer import MachineStyleUpdateSerializer


class MachineStyleSwaggerView(MachineStyleView):
    @swagger_auto_schema(
            tags=['machine_style - Вид оборудования'],
            operation_summary='Создание определённого вид оборудования',
            operation_description='Создёт определённый вид оборудования',
            manual_parameters=[ACCESS_TOKEN_PARAM],
            request_body=MachineStyleCreateSerializer,
            responses={
                200: 'Успешная обработка запроса',
                400: 'Ошибка обработки запроса',
                404: 'Не удалось найти оборудование',
                500: 'Ошибка сервера'
            }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
            tags=['machine_style - Вид оборудования'],
            operation_summary='Вывод списка видов оборудования',
            operation_description='Выводит список видов оборудования',
            manual_parameters=[ACCESS_TOKEN_PARAM],
            responses={
                200: 'Успешная обработка запроса',
                400: 'Ошибка обработки запроса',
                404: 'Не удалось найти оборудование',
                500: 'Ошибка сервера'
            }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
            tags=['machine_style - Вид оборудования'],
            operation_summary='Вывод определённого вида оборудования',
            operation_description='Выводит определённый вид оборудования',
            manual_parameters=[ACCESS_TOKEN_PARAM],
            responses={
                200: 'Успешная обработка запроса',
                400: 'Ошибка обработки запроса',
                404: 'Не удалось найти оборудование',
                500: 'Ошибка сервера'
            }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
            tags=['machine_style - Вид оборудования'],
            operation_summary='Изменение определённого вида оборудования',
            operation_description='Изменяет определённый вид оборудования',
            manual_parameters=[ACCESS_TOKEN_PARAM],
            request_body=MachineStyleUpdateSerializer,
            responses={
                200: 'Успешная обработка запроса',
                400: 'Ошибка обработки запроса',
                404: 'Не удалось найти оборудование',
                500: 'Ошибка сервера'
            }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
            tags=['machine_style - Вид оборудования'],
            operation_summary='Удаление определённого вида оборудования',
            operation_description='Удаляет определённый вид оборудования',
            manual_parameters=[ACCESS_TOKEN_PARAM],
            responses={
                200: 'Успешная обработка запроса',
                400: 'Ошибка обработки запроса',
                404: 'Не удалось найти оборудование',
                500: 'Ошибка сервера'
            }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
