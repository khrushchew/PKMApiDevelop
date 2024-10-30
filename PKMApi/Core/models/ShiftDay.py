from django.db import models


class ShiftDay(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Название дня недели')

    class Meta:
        db_table = 'ShiftDay'
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни недели'

    def __str__(self):
        return f'{self.name}'
    