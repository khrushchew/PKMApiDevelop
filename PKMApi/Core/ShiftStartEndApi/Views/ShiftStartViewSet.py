from django.utils import timezone

from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from rest_framework.permissions import IsAuthenticated

from ..Serializers.ShiftStartSerializer import ShiftStartApiSerializer


class ShiftStartApiViewSet(ViewSet):

    # permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):

        data = timezone.now().strftime('%d-%m-%Y %H:%M:%S')

        serializer = ShiftStartApiSerializer(request.user, data=data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(status=200)
