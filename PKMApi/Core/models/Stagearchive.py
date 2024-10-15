from django.db import models


class Stagearchive(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)
    batch_archive = models.ForeignKey('Batcharchive', models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'Stagearchive'