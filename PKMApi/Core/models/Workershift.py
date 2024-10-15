from django.db import models


class Workershift(models.Model):
    time_start = models.DateTimeField(null=False, blank=False)
    time_end = models.DateTimeField(blank=True, null=True)
    isactive = models.BooleanField(default=False, blank=False, null=False)
    change = models.ForeignKey('Shift', models.DO_NOTHING, blank=True, null=True)
    date = models.DateField()
    staff = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'Workershift'
