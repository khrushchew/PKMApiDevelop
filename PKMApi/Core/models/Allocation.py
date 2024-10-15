from django.db import models


class Allocation(models.Model):
    user = models.ForeignKey('User', models.CASCADE, blank=False, null=False)
    role = models.ForeignKey('Role', models.SET_NULL, blank=True, null=True)
    area = models.ForeignKey('Area', models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'Allocation'