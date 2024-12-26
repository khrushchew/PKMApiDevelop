from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from department.views.department_view import DepartmentView

from ..serializers.department_create_serializer import DepartmentCreateSerializer
from ..serializers.department_retrieve_serializer import DepartmentRetrieveSerializer
from ..serializers.department_list_serializer import DepartmentListSerializer

class DepartmentSwaggerView(DepartmentView):
    access_token_param = openapi.Parameter(
        'Authorization',
        openapi.IN_HEADER,
        description="Код доступа",
        type=openapi.TYPE_STRING,
        required=True,
        default='JWT {token}'
    )

    @swagger_auto_schema(
        tags=['department - Цех'],
        operation_summary='Создание цеха',
        operation_description='Создаёт цех для определённой компании',
        manual_parameters=[access_token_param],
        request_body=DepartmentCreateSerializer,
        responses={
            201: "Успешное создание цеха",
            400: "Ошибка при обработке запроса",
            401: "Ошибка прав доступа",
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['department - Цех'],
        operation_summary='Вывод списка цехов',
        operation_description='Выводит список цехов для определённой компании',
        manual_parameters=[access_token_param],
        responses={
            200: DepartmentListSerializer(many=True),
            400: "Ошибка при обработке запроса",
            401: "Ошибка прав доступа",
            404: "Не найдено ни одного цеха",
            500: "Ошибка сервера"
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
        
    
    @swagger_auto_schema(
        tags=['department - Цех'],
        operation_summary='Вывод определённого цеха',
        operation_description='Выводит определённый цех для определённой компании',
        manual_parameters=[access_token_param],
        responses={
            200: DepartmentRetrieveSerializer,
            400: "Ошибка при обработке запроса",
            401: "Ошибка прав доступа",
            404: "Не найдено такого цеха",
            500: "Ошибка сервера"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
        
    @swagger_auto_schema(
        tags=['department - Цех'],
        operation_summary='Изменение определённого цеха',
        operation_description='Изменяет определённый цех для определённой компании',
        request_body=DepartmentRetrieveSerializer,
        manual_parameters=[access_token_param],
        responses={
            200: "Успешное изменение цеха",
            400: "Ошибка при обработке запроса",
            401: "Ошибка прав доступа",
            404: "Не найдено такого цеха",
            500: "Ошибка сервера"
        }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
        

    @swagger_auto_schema(
        tags=['department - Цех'],
        operation_summary='Удаление определённого цеха',
        operation_description='Удаляет определённый цех для определённой компании',
        manual_parameters=[access_token_param],
        responses={
            200: "Успешное удаление цеха",
            400: "Ошибка при обработке запроса",
            401: "Ошибка прав доступа",
            404: "Не найдено такого цеха",
            500: "Ошибка сервера"
        }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
