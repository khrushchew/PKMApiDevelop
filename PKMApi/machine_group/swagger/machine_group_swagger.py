from drf_yasg.utils import swagger_auto_schema

from Core.swagger_params import ACCESS_TOKEN_PARAM, MACHINE_STYLE_PARAM

from machine_group.views.machine_group_view import MachineGroupView


from machine_group.serializer.machine_group_create_serializer import MachineGroupCreateSerializer
from machine_group.serializer.machine_group_list_serializer import MachineGroupListSerializer
from machine_group.serializer.machine_group_retrieve_serializer import MachineGroupRetrieveSerializer
from machine_group.serializer.machine_group_update_serializer import MachineGroupUpdateSerializer

class MachineGroupSwaggerView(MachineGroupView):
    @swagger_auto_schema(
            tags=['machine_group - Группа оборудования'],
            operation_summary='Создание определённой группы оборудования',
            operation_description='Создёт определённую группу оборудования',
            manual_parameters=[ACCESS_TOKEN_PARAM],
            request_body=MachineGroupCreateSerializer,
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
            tags=['machine_group - Группа оборудования'],
            operation_summary='Вывод списка групп оборудования',
            operation_description='Выводит список групп оборудования',
            manual_parameters=[ACCESS_TOKEN_PARAM, MACHINE_STYLE_PARAM],
            responses={
                200: MachineGroupListSerializer(many=True),
                400: 'Ошибка обработки запроса',
                404: 'Не удалось найти оборудование',
                500: 'Ошибка сервера'
            }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
            tags=['machine_group - Группа оборудования'],
            operation_summary='Вывод определённой группы оборудования',
            operation_description='Выводит определённую группу оборудования',
            manual_parameters=[ACCESS_TOKEN_PARAM],
            responses={
                200: MachineGroupRetrieveSerializer,
                400: 'Ошибка обработки запроса',
                404: 'Не удалось найти оборудование',
                500: 'Ошибка сервера'
            }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
            tags=['machine_group - Группа оборудования'],
            operation_summary='Изменение определённой группы оборудования',
            operation_description='Изменяет определённую группу оборудования',
            manual_parameters=[ACCESS_TOKEN_PARAM],
            request_body=MachineGroupUpdateSerializer,
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
            tags=['machine_group - Группа оборудования'],
            operation_summary='Удаление определённой группы оборудования',
            operation_description='Удаляет определённую группу оборудования',
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
