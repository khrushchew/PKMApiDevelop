from django.db import models


class Transferoperation(models.Model):
    time_first_start = models.DateTimeField(blank=True, null=True)
    time_start = models.DateTimeField(blank=True, null=True)
    time_stop = models.DateTimeField(blank=True, null=True)
    time_working = models.DurationField(blank=True, null=True)
    batch = models.ForeignKey('Batch', models.SET_NULL, blank=True, null=True)
    machine = models.ForeignKey('Machine', models.SET_NULL, blank=True, null=True)
    operation = models.ForeignKey('Operation', models.SET_NULL, blank=True, null=True)
    chief_operation = models.ForeignKey('Chiefoperation', models.SET_NULL, blank=True, null=True)
    pause = models.BooleanField(blank=True, null=True)
    staff = models.ForeignKey('User', models.SET_NULL, blank=True, null=True)
    opt_path = models.TextField(blank=True, null=True)
    transfer = models.ForeignKey('Transfer', models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey('Order', models.SET_NULL, blank=True, null=True)
    operator_operation = models.ForeignKey('Operationoperator', models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'Transferoperation'