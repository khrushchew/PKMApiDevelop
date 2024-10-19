from rest_framework.response import Response
from rest_framework.views import APIView

from ..Serializers.SubdivisionSerializer import SubdivisionApiSerializer
from Core.models.Subdivision import Subdivision
from Core.models.Company import Company

class SubdivisionListCreateApiView(APIView):

    def post(self, request):

        name = request.data.get('name')
        company_code = request.data.get('company_code')

        company = Company.objects.get(code=company_code)

        if Subdivision.objects.filter(name=name, company__code=company_code).exists():
            return Response({'error': 'Подразделение с таким названием уже существует'}, status=409)

        try:
            subdivision = Subdivision.objects.create(name=name, company=company)
            serializer = SubdivisionApiSerializer(subdivision)
            return Response(status=200)
        except:
            return Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    def get(self,request):
        
        company_code = request.query_params.get('company_code')

        try:
            subdivision = Subdivision.objects.filter(company__code=company_code)
            serializer = SubdivisionApiSerializer(subdivision, many=True)
            for i in range(1, len(serializer.data)+1):
                serializer.data[i-1].setdefault("id", i)
            return Response(serializer.data, status=200)
        except:
            return Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)
