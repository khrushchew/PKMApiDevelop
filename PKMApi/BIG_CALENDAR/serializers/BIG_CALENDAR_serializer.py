from Core.models.BIG_CALENDAR import BIG_CALENDAR

from rest_framework import serializers


class BIG_CALENDAR_Api_Serializer(serializers.ModelSerializer):
    class Meta:
        model = BIG_CALENDAR
        fields = ('day',)
