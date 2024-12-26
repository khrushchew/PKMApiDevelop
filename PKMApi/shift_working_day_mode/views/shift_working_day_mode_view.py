from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.permissions import IsAuthenticated

from datetime import datetime, timedelta

from shift_working_day_mode.serializers.shift_working_day_mode_create_serializer import ShiftWorkingDayModeCreateSerializer
from shift_working_day_mode.serializers.shift_working_day_mode_update_serializer import ShiftWorkingDayModeUpdateSerializer
from shift_working_day_mode.serializers.shift_working_day_mode_list_serializer import ShiftWorkingDayModeListSerializer
from shift_working_day_mode.serializers.shift_working_day_mode_retrieve_serializer import ShiftWorkingDayModeRetrieveSerializer

from Core.models.ShiftWorkingDayMode import ShiftWorkingDayMode


class ShiftWorkingDayModeView(ViewSet):

    permission_classes = [IsAuthenticated]
    
    handler200 = Response(status=200)
    handler201 = Response({'detail': 'Режим рабочего дня успешно создан'}, status=201)
    handler500 = Response({'detail': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    @staticmethod
    def format_timedelta(td):
        total_seconds = int(td.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def get_shift_working_day_mode_list(self):
        shift_working_day_modes = ShiftWorkingDayMode.objects.filter(company=self.request.user.company)
        if shift_working_day_modes.exists():
            return shift_working_day_modes
        else:
            raise NotFound({'detail': 'Режимов рабочего дня не найдено'})

    def code_validation(self, code, company):
        if ShiftWorkingDayMode.objects.filter(code=code, company=company).exists():
            raise ValidationError({'detail': 'Такой код режима рабочего дня уже существует'})
    
    def get_shift_working_day_mode_entity(self):
        try:
            return ShiftWorkingDayMode.objects.get(pk=self.kwargs.get('pk'))
        except:
            raise NotFound({'detail': 'Такого режима рабочего дня не найдено'})

    def create(self, request, *args, **kwargs):
        data = request.data

        data['company'] = request.user.company.pk

        serializer = ShiftWorkingDayModeCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        try:
            serializer.save()
            return self.handler201
        except:
            return self.handler500

    def list(self, request, *args, **kwargs):
        shift_working_day_modes = self.get_shift_working_day_mode_list()

        serializer = ShiftWorkingDayModeListSerializer(shift_working_day_modes, many=True)

        data = serializer.data
        pause_sum = timedelta()

        
        for i in data:
            for j in range(1, 11):

                start_time = i.get(f'start_pause_{j}')
                end_time = i.get(f'end_pause_{j}')

                if start_time and end_time:
                    pause_duration = datetime.strptime(end_time, '%H:%M:%S') - datetime.strptime(start_time, '%H:%M:%S')
                    i[f'pause_res_{j}'] = str(pause_duration)
                    pause_sum += pause_duration
                else:
                    i[f'pause_res_{j}'] = None

            start_time = datetime.strptime(i.get('start_time'), '%H:%M:%S')
            end_time = datetime.strptime(i.get('end_time'), '%H:%M:%S')

            work_time = (end_time-start_time)
            no_pause = (end_time-start_time) - pause_sum

            i['pause_sum'] = ShiftWorkingDayModeView.format_timedelta(pause_sum)
            i['no_pause'] = ShiftWorkingDayModeView.format_timedelta(no_pause)
            i['work_time'] = ShiftWorkingDayModeView.format_timedelta(work_time)
        try:
            return Response(data, status=200)
        except:
            return self.handler500
        
    def retrieve(self, request, *args, **kwargs):
        shift_working_day_mode = self.get_shift_working_day_mode_entity()

        serializer = ShiftWorkingDayModeRetrieveSerializer(shift_working_day_mode)
        data = serializer.data

        try:
        # for j in range(1, 11):

        #     start_time = data.get(f'start_pause_{j}')
        #     end_time = data.get(f'end_pause_{j}')
        
        #     if start_time and end_time:
        #         pause_duration = datetime.strptime(end_time, '%H:%M:%S') - datetime.strptime(start_time, '%H:%M:%S')
        #         data[f'pause_res_{j}'] = str(pause_duration)
        #         data['pause_sum'] += pause_duration
        #     else:
        #         data[f'pause_res_{j}'] = None
            return Response(data, status=200)
        except:
            return self.handler500
    
    def update(self, request, *args, **kwargs):
        shift_working_day_mode = self.get_shift_working_day_mode_entity()

        company = request.user.company
        self.code_validation(code=request.data.get('code'), company=company)

        
        serializer = ShiftWorkingDayModeUpdateSerializer(shift_working_day_mode, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        
        try:
            serializer.save()
            return self.handler200
        except:
            return self.handler500

    def destroy(self, request, *args, **kwargs):
        shift_working_day_mode = self.get_shift_working_day_mode_entity()
        try:
            shift_working_day_mode.delete()
            return self.handler200
        except:
            return self.handler500
        