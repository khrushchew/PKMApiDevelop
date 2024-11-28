from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.permissions import IsAuthenticated

from datetime import datetime

from shift_working_day_mode.serializers.shift_working_day_mode_create_serializer import ShiftWorkingDayModeCreateSerializer
from shift_working_day_mode.serializers.shift_working_day_mode_update_serializer import ShiftWorkingDayModeUpdateSerializer
from shift_working_day_mode.serializers.shift_working_day_mode_list_serializer import ShiftWorkingDayModeListSerializer
from shift_working_day_mode.serializers.shift_working_day_mode_retrieve_serializer import ShiftWorkingDayModeRetrieveSerializer

from Core.models.ShiftWorkingDayMode import ShiftWorkingDayMode


class ShiftWorkingDayModeView(ModelViewSet):

    permission_classes = [IsAuthenticated]
    
    handler200 = Response(status=200)
    handler201 = Response({'detail': 'Режим рабочего дня успешно создан'}, status=201)
    handler500 = Response({'detail': 'Что-то пошло не так, повторите попытку позже'}, status=500)

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
        # try:
        serializer = ShiftWorkingDayModeListSerializer(shift_working_day_modes, many=True)

        data = serializer.data

        for i in data:
            for j in range(1, 11):
                
                try:
                    i[f'pause_res_{j}'] = str(datetime.strptime(i[f'end_pause_{j}'], '%H:%M:%S') - datetime.strptime(i[f'start_pause_{j}'], '%H:%M:%S'))
                except:
                    i[f'pause_res_{j}'] = None



        return Response(data, status=200)
        # except:
        #     return self.handler500
        
    def retrieve(self, request, *args, **kwargs):
        shift_working_day_mode = self.get_shift_working_day_mode_entity()
        try:
            serializer = self.get_serializer(shift_working_day_mode)
            return Response(serializer.data, status=200)
        except:
            return self.handler500
    
    def update(self, request, *args, **kwargs):
        shift_working_day_mode = self.get_shift_working_day_mode_entity()

        company = self.get_company()
        self.code_validation(code=request.data.get('code'), company=company)

        try:
            serializer = self.get_serializer(shift_working_day_mode, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
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
        