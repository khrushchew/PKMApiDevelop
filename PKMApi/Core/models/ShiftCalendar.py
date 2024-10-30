from django.db import models


class ShiftCalendar(models.Model):
    day = models.DateField(null=False, blank=False, verbose_name='День недели')
    shift_working_day_mode = models.ForeignKey('ShiftWorkingDayMode', models.PROTECT, null=False, blank=False, verbose_name='Режим рабочего дня')
    shift_mode = models.ForeignKey('ShiftMode', models.PROTECT, null=False, blank=False, verbose_name='Режим сменности')

    class Meta:
        db_table = 'ShiftCalendar'
        verbose_name = 'Календарь'
        verbose_name_plural = 'Календари'

    @staticmethod
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
        return dict[obj]

    def __str__(self):
        return f'{self.day} - {self.int_to_day(str(self.day.weekday()))} - {self.shift_working_day_mode}'
    
    