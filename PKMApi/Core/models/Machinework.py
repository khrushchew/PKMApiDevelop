from django.db import models


class Machinework(models.Model):
    start_time = models.DateTimeField(null=False, blank=False)
    stop_time = models.DateTimeField(blank=True, null=True)
    work_status = models.ForeignKey('Workstatus', models.SET_NULL, blank=True, null=True)
    machine = models.ForeignKey('Machine', models.SET_NULL, blank=True, null=True)
    batch = models.ForeignKey('Batch', models.SET_NULL, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    shift = models.ForeignKey('Shift', models.SET_NULL, blank=True, null=True)
    date = models.DateField(null=False, blank=False)
    indent = models.IntegerField(default=0, blank=False, null=False)
    time_working = models.DurationField(blank=True, null=True)
    isactive = models.BooleanField(blank=True, null=True)
    first_start_batch = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('User', models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'Machinework'