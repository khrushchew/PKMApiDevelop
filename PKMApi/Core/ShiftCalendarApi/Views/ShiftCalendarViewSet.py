from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import NotFound, ValidationError

from ..Serializer.ShiftCalendarSerializer import ShiftCalendarApiSerializer

from Core.models import Company

from Core.models.ShiftCalendar import ShiftCalendar

from Core.models.ShiftMode import ShiftMode
from Core.models.ShiftWorkingDayMode import ShiftWorkingDayMode

from datetime import date


class ShiftCalendarApiViewSet(ModelViewSet):
    
    serializer_class = ShiftCalendarApiSerializer

    handler200 = Response(status=200)
    handler500 = Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    def get_company(self):
        company_code = self.kwargs.get('company_code')
        try:
            return Company.objects.get(code=company_code)
        except:
            raise NotFound({'error': 'Такой компании не найдено'})

    def get_shift_mode(self):
        shift_mode_code = self.request.query_params.get('shift_mode_code')
        if shift_mode_code:
            try:
                return ShiftMode.objects.get(code=shift_mode_code, company=self.get_company())
            except ShiftMode.DoesNotExist:
                raise NotFound({'error': 'Такого режима смености не найдено'})
        else:
            shift_mode_code = self.request.data.get('shift_mode_code')
            try:
                return ShiftMode.objects.get(code=shift_mode_code, company=self.get_company())
            except ShiftMode.DoesNotExist:
                raise NotFound({'error': 'Такого режима смености не найдено'})
            
    def get_shift_calendar_list(self):
        shift_calendars = ShiftCalendar.objects.filter(shift_mode=self.get_shift_mode()).order_by('day')
        if shift_calendars.exists():
            return shift_calendars
        else:
            raise NotFound({'error': 'Расписаний не найдено'})

    def get_shift_working_day_mode(self):
        company_code = self.kwargs.get('company_code')
        shift_working_day_mode_code = self.request.data.get('shift_working_day_mode_code')
        try:
            return ShiftWorkingDayMode.objects.get(code=shift_working_day_mode_code, company__code=company_code)
        except:
            return self.handler500
    
    def get_shift_calendar_entity(self):
        try:
            return ShiftCalendar.objects.get(pk=self.kwargs.get('pk'))
        except:
            raise NotFound({'error': 'Такого расписания не найдено'})

    def create(self, request, *args, **kwargs):
        company = self.get_company()

        data ={"day": date.fromisoformat(request.data.get('day')),
                "shift_working_day_mode": str(self.get_shift_working_day_mode().pk),
                "shift_mode": str(self.get_shift_mode().pk)
                }

        serializer = self.get_serializer(data=data)
        print(data)
        serializer.is_valid(raise_exception=True)

        try:
            serializer.save()
            return self.handler200
        except:
            return self.handler500

    def list(self, request, *args, **kwargs):
        
        def int_to_day(obj):
            dict = {
                '0': 'Понедельник',
                '1': 'Вторник',
                '2': 'Среда',
                '3': 'Четверг',
                '4': 'Пятница',
                '5': 'Суббота',
                '6': 'Воскресенье',
            }
            return dict[str(obj)]

        shift_calendars = self.get_shift_calendar_list()
        try:
            serializer = self.get_serializer(shift_calendars, many=True)
            data = serializer.data
            for i in data:
                i['day_name'] = int_to_day(date.fromisoformat(i['day']).weekday())
                mode = ShiftWorkingDayMode.objects.get(pk=i['shift_working_day_mode'])
                i['shift_working_day_mode'] = f"{mode.start_time.strftime("%H:%M")} - {mode.end_time.strftime("%H:%M")}"
                i.pop('shift_mode')
            return Response(data, status=200)
        except:
            return self.handler500
        
    def update(self, request, *args, **kwargs):
        shift_calendar = self.get_shift_calendar_entity()
        data ={"shift_working_day_mode": str(self.get_shift_working_day_mode().pk)}
        try:
            serializer = self.get_serializer(shift_calendar, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return self.handler200
        except:
            return self.handler500

    def destroy(self, request, *args, **kwargs):
        shift_calendar = self.get_shift_calendar_entity()
        try:
            shift_calendar.delete()
            return self.handler200
        except:
            return self.handler500
        