from rest_framework.viewsets import ViewSet
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import Group

from Core.models.Allocation import Allocation

from ..Serializers.RoleListSerializer import RoleListApiSerializer
from ..Serializers.RoleCreateSerializer import RoleCreateApiSerializer

class RoleApiViewSet(ViewSet):

    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        group = Group.objects.all().order_by('name')
        serializer = RoleListApiSerializer(group, many=True)
        if not serializer.data:
            raise NotFound({'detail': 'Ролей не найдено'})
        return Response(serializer.data, status=200)


    def create(self, request, *args, **kwargs):
        data = request.data
        data['user'] = request.user.pk
        serializer = RoleCreateApiSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'detail': 'Роль успешно создана'}, status=201)
