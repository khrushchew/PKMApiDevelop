from django.db import models


class Chiefbatch(models.Model):
    bath = models.ForeignKey('Batch', models.SET_NULL, blank=True, null=True)
    batch_status = models.ForeignKey('Batchstatus', models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'Chiefbatch'