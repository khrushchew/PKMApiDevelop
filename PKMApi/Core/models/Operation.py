from django.db import models


class Operation(models.Model):
    number = models.IntegerField(default=0, null=False, blank=False)
    name = models.CharField(null=False, blank=False, max_length=255)
    code = models.CharField(max_length=50, blank=True, null=True)
    time_pz = models.DurationField(blank=True, null=True)
    time_sh = models.DurationField(blank=True, null=True)
    stage = models.ForeignKey('Stage', models.CASCADE, blank=False, null=False)

    class Meta:
        db_table = 'Operation'