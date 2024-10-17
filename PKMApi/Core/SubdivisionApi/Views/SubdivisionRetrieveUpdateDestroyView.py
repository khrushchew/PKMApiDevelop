from rest_framework.response import Response
from rest_framework.views import APIView

from ..Serializers.SubdivisionSerializer import SubdivisionApiSerializer

from Core.models.Subdivision import Subdivision


class SubdivisionRetrieveUpdateDestroyApiView(APIView):
    
    def put(self, request, pk):

        name = request.data.get('name')

        try:
            subdivision = Subdivision.objects.get(pk=pk)
        except:
            return Response({'error': 'Подразделение не найдено'}, status=404)
        
        # Проверка на дублирование

        try:
            subdivision.name = name
            subdivision.save()
            return Response(status=200)
        except:
            return Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    def get(self, request, pk):
        
        try:
            subdivision = Subdivision.objects.get(pk=pk)
        except:
            return Response({'error': 'Подразделение не найдено'}, status=404)

        try:
            serializer = SubdivisionApiSerializer(subdivision)
            return Response(serializer.data, status=200)
        except:
            return Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)
        
    def delete(self, request, pk):
        
        try:
            subdivision = Subdivision.objects.get(pk=pk)
        except:
            return Response({'error': 'Подразделение не найдено'}, status=404)

        try:
            subdivision.delete()
            return Response(status=200)
        except:
            return Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)
        
   

    