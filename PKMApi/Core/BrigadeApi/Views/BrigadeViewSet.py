from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from ..Serializers.BrigadeSerializer import BrigadeApiSerializer
from ..Serializers.BrigadeListSerializer import BrigadeListApiSerializer

from Core.models.Company import Company
from Core.models.Brigade import Brigade


class BrigadeApiViewSet(ViewSet):
    def get_brigades_list(self):
        brigades = Brigade.objects.filter(company__code=self.kwargs.get('company_code')).order_by('name')
        if brigades.exists():
            return brigades
        else:
            return Response({'error': 'Бригад не найдено'}, status=404)

    def create(self, request, *args, **kwargs):

        data = request.data

        pk = Company.objects.get(code=self.kwargs.get('company_code')).pk
        data['company'] = pk

        serializer = BrigadeApiSerializer(data=data)
        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=200)

    def list(self, request, *args, **kwargs):
        
        brigades = self.get_brigades_list()

        serializer = BrigadeListApiSerializer(brigades, many=True)

        for item in serializer.data:
            print(item.get('area'))
        
        
        return Response(serializer.data, status=200)
    