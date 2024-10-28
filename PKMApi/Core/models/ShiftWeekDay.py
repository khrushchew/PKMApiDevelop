from django.db import models


class ShiftWeekDay(models.Model):
    name = models.DateField(max_length=50, null=False, blank=False, verbose_name='День')

    class Meta:
        db_table = 'ShiftWeekDay'