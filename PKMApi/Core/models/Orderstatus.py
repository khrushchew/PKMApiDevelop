from django.db import models


class Orderstatus(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)

    class Meta:
        db_table = 'Orderstatus'