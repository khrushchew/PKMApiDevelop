from django.db import models


class Allocation(models.Model):
    user = models.ForeignKey('User', models.CASCADE, blank=False, null=False)
    area = models.ForeignKey('Area', models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'Allocation'