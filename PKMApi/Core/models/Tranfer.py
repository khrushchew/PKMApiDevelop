from django.db import models


class Transfer(models.Model):
    number = models.IntegerField(default=0, null=False, blank=False)
    time_sh = models.DurationField(blank=True, null=True)
    operation = models.ForeignKey('Operation', models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'Transfer'
