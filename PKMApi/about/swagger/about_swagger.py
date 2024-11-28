
from about.views.about_view import AboutView
from Core.swagger_params import ACCESS_TOKEN_PARAM
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class AboutSwaggerView(AboutView):

    @swagger_auto_schema(
        operation_summary="Вывод информации о приложении",
        operation_description="Получает текущую информацию о приложении, включая версию, дату обновления, разработчика и контактные данные.",
        tags=['about'],
        responses={
            200: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'about application': openapi.Schema(type=openapi.TYPE_STRING, description='О приложении'),
                    "contacts": openapi.Schema(type=openapi.TYPE_STRING, description='Контакты'),
                    "info": openapi.Schema(type=openapi.TYPE_STRING, description="Некоторая правовая информация"),
                    "instructions": openapi.Schema(type=openapi.TYPE_STRING, description="Некоторые инструкции"),
                    }
                    ),
            404: openapi.Response(description="Неверное значение запроса"),
            }
        )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    