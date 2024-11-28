from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.utils import timezone

from shift.serializers.shift_start_serializer import ShiftStartSerializer


class ShiftStartView(ViewSet):
    
    permission_classes = [IsAuthenticated]

    handler200 = Response(status=200)
    handler500 = Response({'detail': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    def update(self, request, *args, **kwargs):
        data = {'start_shift': timezone.now()}
        serializer = ShiftStartSerializer(request.user, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        data['start_shift'] =  data['start_shift'].strftime('%d-%m-%Y %H:%M:%S')
        try:
            serializer.save()
            return Response(data, status=200)
        except:
            return self.handler500
