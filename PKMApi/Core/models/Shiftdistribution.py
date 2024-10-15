from django.db import models


class Shiftdistribution(models.Model):
    date = models.DateField(null=False, blank=False)
    change = models.ForeignKey('Shift', models.SET_NULL, blank=True, null=True)
    machine = models.ForeignKey('Machine', models.SET_NULL, blank=True, null=True)
    staff = models.ForeignKey('User', models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'Shiftdistribution'
