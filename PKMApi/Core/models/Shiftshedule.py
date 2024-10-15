from django.db import models


class Shiftschedule(models.Model):
    time_change = models.TimeField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    time_first = models.TimeField(blank=True, null=True)
    days = models.IntegerField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'Shiftschedule'
