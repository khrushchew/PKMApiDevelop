from django.db import models


class Transferarchive(models.Model):
    time_sh = models.DurationField(blank=True, null=True)
    operation_archive = models.ForeignKey('Operationarchive', models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'Transferarchive'
