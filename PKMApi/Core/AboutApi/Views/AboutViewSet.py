from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ..Serializers.AboutSerializer import AboutSerializer

from Core.models.About import About


class AboutApiViewSet(ModelViewSet):
    serializer_class = AboutSerializer

    def list(self, request, *args, **kwargs):
        about = About.objects.all()
        serializer = self.get_serializer(about, many=True)
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
            "Инструкции": data[0]['instruction'],
        }
        return Response(result, status=200)
    