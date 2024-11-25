from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated

from about.serializers.about_serializer import AboutSerializer

from Core.models.About import About


class AboutView(ViewSet):

    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        about = About.objects.all()
        serializer = AboutSerializer(about, many=True)
        data = serializer.data
        result = {
            "about application": {
                "version": '123',
                "update": '566',
                "developer": "ООО ПКМ"        
            },
            "contacts": {
                "address": ''
            },
            "info": '',
            "instructions": '',
        }
        return Response(result, status=200)
    