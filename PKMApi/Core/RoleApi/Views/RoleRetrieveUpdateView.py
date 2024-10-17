from rest_framework.response import Response
from rest_framework.views import APIView

from ..Serializers.RoleSerializer import RoleApiSerializer

from Core.models.Role import Role


class RoleRetrieveUpdateApiView(APIView):

    def put(self, request, pk):

        name = request.data.get('name')

        try:
            role = Role.objects.get(pk=pk)
        except:
            return Response({'error': 'Такой роли не найдено'}, status=404)

        # proverka

        try:
            role.name = name
            role.save()
            return Response(status=200)
        except:
            return Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)
        

    def delete(self, request, pk):

        try:
            role = Role.objects.get(pk=pk)
        except:
            return Response({'error': 'Такой роли не найдено'}, status=404)

        try:
            role.delete()
            return Response(status=200)
        except:
            return Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)
        

    def get(self, request, pk):

        try:
            role = Role.objects.get(pk=pk)
        except:
            return Response({'error': 'Такой роли не найдено'}, status=404)
        
        try:
            serializer = RoleApiSerializer(role)
            return Response(serializer.data, status=200)
        except:
            return Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)
