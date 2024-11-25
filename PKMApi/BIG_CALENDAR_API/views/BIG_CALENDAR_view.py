from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from datetime import date, timedelta

from BIG_CALENDAR_API.serializers.BIG_CALENDAR_serializer import BIG_CALENDAR_Api_Serializer


class BIG_CALENDAR_Api_View(ViewSet):
    
    permission_classes = [IsAdminUser]

    start_date = date(year=2025, month=1, day=1)

    def create(self, request, *args, **kwargs):
        for i in range(365):
            current_date = self.start_date + timedelta(days=i)

            serializer = BIG_CALENDAR_Api_Serializer(data={'day': current_date})
            serializer.is_valid(raise_exception=True)
            serializer.save()

        return Response(status=201)
