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
    