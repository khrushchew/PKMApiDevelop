from django.db import models


class Stage(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)
    isdistributed = models.BooleanField(default=False, blank=False, null=False)
    area = models.ForeignKey('Area', models.SET_NULL, blank=True, null=True)
    batch = models.ForeignKey('Batch', models.SET_NULL, blank=True, null=True)
    batch_archive = models.ForeignKey('Batcharchive', models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'Stage'