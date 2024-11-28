from rest_framework import serializers

from Core.models.ShiftWorkingDayMode import ShiftWorkingDayMode


class ShiftWorkingDayModeRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShiftWorkingDayMode
        fields = ('pk', 'code', 'name', 'company', 'start_time', 'end_time', 
                  'start_pause_1', 'end_pause_1',
                  'start_pause_2', 'end_pause_2',
                  'start_pause_3', 'end_pause_3',
                  'start_pause_4', 'end_pause_4',
                  'start_pause_5', 'end_pause_5',
                  'start_pause_6', 'end_pause_6',
                  'start_pause_7', 'end_pause_7',
                  'start_pause_8', 'end_pause_8',
                  'start_pause_9', 'end_pause_9',
                  'start_pause_10', 'end_pause_10')
