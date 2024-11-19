from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ..Serializers.AboutSerializer import AboutSerializer

from Core.models.About import About


class AboutApiViewSet(ViewSet):

    @swagger_auto_schema(
        operation_summary="Вывод информации о приложении",
        operation_description="Получает текущую информацию о приложении, включая версию, дату обновления, разработчика и контактные данные.",
        tags=['about'],
        responses={
            200: openapi.Response(
                description="Успешный ответ",
                examples={
                    "application/json": {
                        "about application": {
                            "version": "1.0",
                            "update": "2024-01-01",
                            "developer": "ООО ПКМ"
                        },
                        "contacts": {
                            "address": "ул. Пример, д. 1"
                        },
                        "info": "Некоторая правовая информация",
                        "instructions": "Некоторые инструкции"
                    }
                }
            ),
            404: openapi.Response(description="Неверное значение запроса"),
        },
    )
    def list(self, request, *args, **kwargs):
        about = About.objects.all()
        serializer = AboutSerializer(about, many=True)
        data = serializer.data
        result = {
            "about application": {
                "version": data[0]['version'],
                "update": data[0]['upd'],
                "developer": "ООО ПКМ"        
            },
            "contacts": {
                "address": data[0]['address']
            },
            "info": data[0]['info'],
            "instructions": data[0]['instruction'],
        }
        return Response(result, status=200)
    