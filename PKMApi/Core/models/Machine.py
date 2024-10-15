from django.db import models


class Machine(models.Model):
    invent_number = models.CharField(null=False, blank=False, unique=True, max_length=100)
    name = models.CharField(null=False, blank=False, max_length=255)
    area = models.ForeignKey('Area', models.SET_NULL, blank=True, null=True)
    is_activated = models.BooleanField(default=False, blank=False, null=False)
    model = models.CharField(max_length=255, blank=True, null=True)
    shift_schedule = models.ForeignKey('Shiftschedule', models.SET_NULL, blank=True, null=True)
    prefix = models.CharField(max_length=50, blank=True, null=True)
    first_machine_type = models.ForeignKey('Firstmachinetype', models.SET_NULL, blank=True, null=True)
    second_machine_type = models.ForeignKey('Secondmachinetype', models.SET_NULL, blank=True, null=True)
    detail_machine_type = models.ForeignKey('Detailmachinetype', models.SET_NULL, blank=True, null=True)
 
    class Meta:
        db_table = 'Machine'