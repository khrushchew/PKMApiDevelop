from django.db import models


class Chiefoperation(models.Model):
    chief_batch = models.ForeignKey('Chiefbatch', models.CASCADE, blank=False, null=False)
    stage = models.ForeignKey('Stage', models.SET_NULL, blank=True, null=True)
    operation = models.ForeignKey('Operation', models.SET_NULL, blank=True, null=True)
    is_distributed = models.BooleanField(default=False, blank=False, null=False)
    distribution_stage = models.ForeignKey('Stagedistribution', models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'Chiefoperation'