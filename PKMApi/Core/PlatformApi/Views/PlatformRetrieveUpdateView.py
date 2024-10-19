from rest_framework.response import Response
from rest_framework.views import APIView

from ..Serializers.PlatformSerializer import PlatformApiSerializer

from Core.models.Platform import Platform


class PlatformRetrieveUpdateApiView(APIView):

    def patch(self, request, pk):

        indent = request.data.get('indent')
        name = request.data.get('name')
        address = request.data.get('address')
        company_code = request.data.get('company_code')

        try:
            platform = Platform.objects.get(pk=pk)
        except:
            return Response({'error': 'Такой платформы не найдено'}, status=404)
        
        if Platform.objects.filter(name=name, company__code=company_code).exists():
            return Response({'error': 'Платформа с таким названием уже существует'}, status=409)

        try:
            if indent:
                platform.indent = indent
            if name:
                platform.name = name
            if address:
                platform.address = address
            platform.save()
            return Response(status=200)
        except:
            return Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)
        
    def delete(self, request, pk):

        try:
            platform = Platform.objects.get(pk=pk)
        except:
            return Response({'error': 'Такой платформы не найдено'}, status=404)
        
        try:
            platform.delete()
            return Response(status=200)
        except:
            return Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)
        
    def get(self, request, pk):

        try:
            platform = Platform.objects.get(pk=pk)
        except:
            return Response({'error': 'Такой платформы не найдено'}, status=404)
        
        try:
            serializer =PlatformApiSerializer(platform)
            return Response(serializer.data, status=200)
        except:
            return Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)
