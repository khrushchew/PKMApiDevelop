from rest_framework.views import APIView
from rest_framework.response import Response

from ..Serializers.PlatformSerializer import PlatformApiSerializer

from Core.models.Platform import Platform
from Core.models.Company import Company

class PlatformListCreateApiView(APIView):
    
    def post(self, request):
        
        indent = request.data.get('indent')
        name = request.data.get('name')
        address = request.data.get('address')
        company_code = request.data.get('company_code')

        company = Company.objects.get(code=company_code)

        if Platform.objects.filter(name=name, company__code=company_code).exists():
            return Response({'error': 'Платформа с таким названием уже существует'}, status=409)

        try:
            Platform.objects.create(indent=indent, name=name, address=address, company=company)
            return Response(status=200)
        except:
            return Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    def get(self, request):

        company_code = request.query_params.get('company_code')

        try:
            role = Platform.objects.filter(company__code=company_code)
            serializer = PlatformApiSerializer(role, many=True)
            return Response(serializer.data, status=200)
        except:
            return Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)