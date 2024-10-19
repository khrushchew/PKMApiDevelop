from rest_framework.response import Response
from rest_framework.views import APIView

from ..Serializers.RoleSerializer import RoleApiSerializer

from Core.models.Role import Role
from Core.models.Company import Company


class RoleListCreateApiView(APIView):

    def post(self, request):

        name = request.data.get('name')
        company_code = request.data.get('company_code')

        company = Company.objects.get(code=company_code)

        if Role.objects.filter(name=name, company__code=company_code).exists():
            return Response({'error': 'Роль с таким названием уже'}, status=409)

        try:
            Role.objects.create(name=name, company=company)
            return Response(status=200)
        except:
            return Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)
        
    def get(self, request):
        
        company_code = request.query_params.get('company_code')

        company = Company.objects.get(code=company_code)

        try:
            role = Role.objects.filter(company=company)
            serializer = RoleApiSerializer(role, many=True)
            for i in range(1, len(serializer.data)+1):
                serializer.data[i-1].setdefault("id", i)
            return Response(serializer.data, status=200)
        except:
            return Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)