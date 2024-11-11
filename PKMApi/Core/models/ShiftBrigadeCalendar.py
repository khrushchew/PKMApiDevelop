from django.db import models


class ShiftBrigadeCalendar(models.Model):
    brigade = models.ForeignKey('Brigade', models.CASCADE, null=False, blank=False, verbose_name='Бригада')
    day = models.ForeignKey('ShiftDay', models.SET_NULL, null=True, blank=True, verbose_name='День недели')
    shift_working_day_mode = models.ForeignKey('ShiftWorkingDayMode', models.PROTECT, null=True, blank=True, verbose_name='Режим рабочего дня')
    shift_mode = models.ForeignKey('ShiftMode', models.PROTECT, null=False, blank=False, verbose_name='Режим сменности')

    class Meta:
        db_table = 'ShiftBrigadeCalendar'
        verbose_name = 'Календарь бригады'
        verbose_name_plural = 'Календари бригад'

    def __str__(self):
        return f'{self.day} - {self.shift_working_day_mode}'
    
    