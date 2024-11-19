from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.viewsets import ViewSet

from ..Serializers.ShiftCreateSerializer import ShiftCreateApiSerializer


class ShiftApiViewSet(ViewSet):
    
    handler201 = Response(status=201)

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = ShiftCreateApiSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return self.handler201
    
    