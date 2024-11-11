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
                        "О приложении": {
                            "Текущая версия": "1.0",
                            "Обновление от": "2024-01-01",
                            "Разработчик": "ООО ПКМ"
                        },
                        "Контакты": {
                            "Адрес": "ул. Пример, д. 1"
                        },
                        "Правовая информация": "Некоторая правовая информация",
                        "Инструкции": "Некоторые инструкции"
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
            "О приложении": {
                "Текущая версия": data[0]['version'],
                "Обновление от": data[0]['upd'],
                "Разработчик": "ООО ПКМ"        
            },
            "Контакты": {
                "Адрес": data[0]['address']
            },
            "Правовая информация": data[0]['info'],
            "Инcтрукции": data[0]['instruction'],
        }
        return Response(result, status=200)
    