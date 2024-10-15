from django.db import models


class Secondmachinetype(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)

    class Meta:
        db_table = 'Secondmachinetype'