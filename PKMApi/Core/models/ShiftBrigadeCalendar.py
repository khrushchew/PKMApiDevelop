from django.db import models


class ShiftBrigadeCalendar(models.Model):
    day = models.ForeignKey('ShiftDay', models.SET_NULL, null=True, blank=True, verbose_name='День недели')
    shift_mode = models.ForeignKey('ShiftMode', models.PROTECT, null=False, blank=False, verbose_name='Режим сменности')
    shift = models.ForeignKey('Shift', models.PROTECT, null=True, blank=True, verbose_name='Смена')

    class Meta:
        db_table = 'ShiftBrigadeCalendar'
        verbose_name = 'Календарь бригады'
        verbose_name_plural = 'Календари бригад'

    def __str__(self):
        return f'{self.day} - {self.shift_working_day_mode}'
    