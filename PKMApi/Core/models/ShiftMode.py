from django.db import models


class ShiftMode(models.Model):
    code = models.CharField(max_length=100, null=False, blank=False, verbose_name='Код режима сменности')
    work_hours_per_day = models.PositiveIntegerField(null=False, blank=False, verbose_name='Рабочих часов в день')
    shifts_per_day = models.PositiveIntegerField(null=False, blank=False, verbose_name='Смен в сутках')
    hours_in_shifts = models.PositiveIntegerField(null=False, blank=False, verbose_name='Часов в смене')
    work_days_inline = models.PositiveIntegerField(null=False, blank=False, verbose_name='Рабочих дней в подряд')
    weekends_inline = models.PositiveIntegerField(null=False, blank=False, verbose_name='Выходных дней в подряд')
    shift_working_day_mode = models.ForeignKey('ShiftWorkingDayMode', models.SET_NULL, null=True, blank=True, verbose_name='Режимы рабочего дня')
    work_days_per_week = models.PositiveIntegerField(null=False, blank=False, verbose_name='Рабочих дней в неделе')
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Наименование')

    class meta:
        db_table = 'ShiftMode'
        verbose_name = 'Режим сменности'
        verbose_name_plural = 'Режимы сменности'

    def __str__(self):
        return f'{self.code}'
    
