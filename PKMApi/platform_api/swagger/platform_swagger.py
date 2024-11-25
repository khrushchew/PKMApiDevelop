from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from platform_api.views.platform_view import PlatformView

from ..serializers.platform_create_serializer import PlatformCreateSerializer
from ..serializers.platform_update_serializer import PlatformUpdateSerializer



class PlatformSwaggerView(PlatformView):

    access_token_param = openapi.Parameter(
        'access_token',
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
        request_body=PlatformCreateSerializer,
        manual_parameters=[access_token_param],
        responses={
            201: "Успешное создание площадки",
            400: "Ошибка при обработке запроса",
            401: "Ошибка прав доступа",
            500: "Ошибка сервера"
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
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
        return super().list(request, *args, **kwargs)

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
        return super().retrieve(request, *args, **kwargs)

        
    @swagger_auto_schema(
        tags=['platform - Площадка'],
        operation_summary = 'Изменение определённой площадки',
        operation_description= 'Меняет определённую площадку для определённой компании',
        manual_parameters=[access_token_param],
        request_body=PlatformUpdateSerializer,
        responses={
            200: "Успешное изменение",
            400: "Ошибка при обработке запроса",
            401: "Ошибка прав доступа",
            404: "Площадки не найдено",
            500: "Ошибка сервера"
        }
    )    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

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
        return super().destroy(request, *args, **kwargs)
