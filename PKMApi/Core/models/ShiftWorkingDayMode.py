from django.db import models


class ShiftWorkingDayMode(models.Model):
    code = models.CharField(max_length=100, null=False, blank=False, verbose_name='Код рабочего дня')
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Названние режима рабочего дня')
    company = models.ForeignKey('Company', models.CASCADE, null=False, blank=False, verbose_name='Компания')
    
    start_time = models.TimeField(null=False, blank=False, verbose_name='Время начала смены')
    end_time = models.TimeField(null=False, blank=False, verbose_name='Время конца смены')

    start_pause_1 = models.TimeField(null=True, blank=True, verbose_name='Начало перерыва 1')
    end_pause_1 = models.TimeField(null=True, blank=True, verbose_name='Начало перерыва 1')

    start_pause_2 = models.TimeField(null=True, blank=True, verbose_name='Начало перерыва 2')
    end_pause_2 = models.TimeField(null=True, blank=True, verbose_name='Начало перерыва 2')

    start_pause_3 = models.TimeField(null=True, blank=True, verbose_name='Начало перерыва 3')
    end_pause_3 = models.TimeField(null=True, blank=True, verbose_name='Начало перерыва 3')

    start_pause_4 = models.TimeField(null=True, blank=True, verbose_name='Начало перерыва 4')
    end_pause_4 = models.TimeField(null=True, blank=True, verbose_name='Начало перерыва 4')

    start_pause_5 = models.TimeField(null=True, blank=True, verbose_name='Начало перерыва 5')
    end_pause_5 = models.TimeField(null=True, blank=True, verbose_name='Начало перерыва 5')

    start_pause_6 = models.TimeField(null=True, blank=True, verbose_name='Начало перерыва 6')
    end_pause_6 = models.TimeField(null=True, blank=True, verbose_name='Начало перерыва 6')

    start_pause_7 = models.TimeField(null=True, blank=True, verbose_name='Начало перерыва 7')
    end_pause_7 = models.TimeField(null=True, blank=True, verbose_name='Начало перерыва 7')

    start_pause_8 = models.TimeField(null=True, blank=True, verbose_name='Начало перерыва 8')
    end_pause_8 = models.TimeField(null=True, blank=True, verbose_name='Начало перерыва 8')

    start_pause_9 = models.TimeField(null=True, blank=True, verbose_name='Начало перерыва 9')
    end_pause_9 = models.TimeField(null=True, blank=True, verbose_name='Начало перерыва 9')

    start_pause_10 = models.TimeField(null=True, blank=True, verbose_name='Начало перерыва 10')
    end_pause_10 = models.TimeField(null=True, blank=True, verbose_name='Начало перерыва 10')

    class Meta:
        db_table = 'ShiftWorkingDayMode'
        verbose_name = 'Режим рабочего дня'
        verbose_name_plural = 'Режимы рабочего дня'