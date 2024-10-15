from django.db import models


class Uploadedreport(models.Model):
    number = models.CharField(default=0, null=False, blank=False, max_length=100)
    staff = models.ForeignKey('User', models.SET_NULL, blank=True, null=True)
    report_type = models.ForeignKey('Reporttype', models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'Uploadedreport'