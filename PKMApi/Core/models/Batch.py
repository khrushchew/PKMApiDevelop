from django.db import models


class Batch(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)
    count = models.IntegerField(default=0, null=False, blank=False)
    code = models.CharField(unique=True, max_length=100, blank=True, null=True)
    technology = models.TextField(blank=True, null=True)
    isready = models.BooleanField(default=False, blank=False, null=False)
    order = models.ForeignKey('Order', models.SET_NULL, blank=True, null=True)
    bath_archive = models.ForeignKey('Batcharchive', models.SET_NULL, blank=True, null=True)
    batch_status = models.ForeignKey('Batchstatus', models.SET_NULL, blank=True, null=True)
    rs_number = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'Batch'