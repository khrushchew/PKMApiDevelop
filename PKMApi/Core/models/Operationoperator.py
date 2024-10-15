from django.db import models


class Operationoperator(models.Model):
    time_plan = models.DurationField(blank=True, null=True)
    time_first_start = models.DateTimeField(blank=True, null=True)
    time_start = models.DateTimeField(blank=True, null=True)
    time_stop = models.DateTimeField(blank=True, null=True)
    time_working = models.DurationField(blank=True, null=True)
    stage_status = models.ForeignKey('Stagestatus', models.SET_NULL, blank=True, null=True)
    batch = models.ForeignKey('Batch', models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey('Order', models.SET_NULL, blank=True, null=True)
    machine = models.ForeignKey('Machine', models.SET_NULL, blank=True, null=True)
    operation = models.ForeignKey('Operation', models.SET_NULL, blank=True, null=True)
    area = models.ForeignKey('Area', models.SET_NULL, blank=True, null=True)
    chief_operation = models.ForeignKey('Chiefoperation', models.SET_NULL, blank=True, null=True)
    chief_batch = models.ForeignKey('Chiefbatch', models.SET_NULL, blank=True, null=True)
    pause = models.BooleanField(blank=True, null=True)
    optimal_part = models.CharField(max_length=255, blank=True, null=True)
    modific = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    distribution_stage = models.ForeignKey('Stagedistribution', models.SET_NULL, blank=True, null=True)
    staff = models.ForeignKey('User', models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'Operationoperator'