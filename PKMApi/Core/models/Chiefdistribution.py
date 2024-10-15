from django.db import models


class Chiefdistribution(models.Model):
    stage = models.ForeignKey('Stage', models.DO_NOTHING, blank=True, null=True)
    operation = models.ForeignKey('Operation', models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=False, null=False)
    batch = models.ForeignKey('Batch', models.SET_NULL, blank=True, null=True)
    unit = models.ForeignKey('Department', models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'Chiefdistribution'