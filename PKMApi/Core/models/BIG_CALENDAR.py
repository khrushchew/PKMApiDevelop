from django.db import models


class BIG_CALENDAR(models.Model):
    day = models.DateField(null=False, blank=False, verbose_name='ДАТА')

    class Meta:
        db_table = 'BIG_CALENDAR'
        verbose_name = 'КАЛЕНДАРЬ'
        verbose_name_plural = 'КАЛЕНДАРЬ'

    def __str__(self):
        return self.day.strftime('%d-%m-%Y')
