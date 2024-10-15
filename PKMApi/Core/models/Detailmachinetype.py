from django.db import models


class Detailmachinetype(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)
    first_machine_type = models.ForeignKey('Firstmachinetype', models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'Detailmachinetype'