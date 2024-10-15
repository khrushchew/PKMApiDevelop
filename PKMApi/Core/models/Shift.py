from django.db import models


class Shift(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)
    number = models.IntegerField(default=0, blank=False, null=False)

    class Meta:
        db_table = 'Shift'