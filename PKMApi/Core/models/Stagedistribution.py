from django.db import models


class Stagedistribution(models.Model):
    stage = models.ForeignKey('Stage', models.CASCADE, blank=False, null=False)
    chief_batch = models.ForeignKey('Chiefbatch', models.SET_NULL, blank=True, null=True)
    stage_status = models.ForeignKey('Stagestatus', models.SET_NULL, blank=True, null=True)
    department = models.ForeignKey('Department', models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'Stagedistribution'