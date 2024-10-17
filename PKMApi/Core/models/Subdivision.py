from django.db import models


class Subdivision(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False, verbose_name='Название подразделения')
    company = models.ForeignKey('Company', models.PROTECT, null=True, blank=True, verbose_name='Компания')

    class Meta:
        db_table='Subdivision'
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

    
    def __str__(self):
        return f"{self.name}"