from django.db import models


class Operationarchive(models.Model):
    number = models.IntegerField(default=0, null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    code = models.CharField(max_length=50, null=False, blank=False)
    time_pz = models.DurationField(blank=True, null=True)
    time_sh = models.DurationField(blank=True, null=True)
    stage_archive = models.ForeignKey('Stagearchive', models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'Operationarchive'