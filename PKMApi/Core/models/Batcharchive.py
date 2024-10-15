from django.db import models


class Batcharchive(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)
    number = models.CharField(default=0, null=False, blank=False, unique=True, max_length=100)
    technology_number = models.CharField(max_length=100, blank=True, null=True)
    company = models.ForeignKey('Company', models.CASCADE, blank=False, null=False)
    code = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'Batcharchive'