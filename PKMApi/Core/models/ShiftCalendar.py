from django.db import models

class ShiftCalendar(models.Model):
    day = models.ForeignKey('ShiftWeekDay', models.SET_NULL, null=True, blank=True, verbose_name='День недели')
    shift = models.ForeignKey('ShiftWorkingDayMode', models.SET_NULL, null=True, blank=True, verbose_name='Смена')
