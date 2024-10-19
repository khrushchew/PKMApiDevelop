from django.db import models


class MachineType(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название')
    group = models.ForeignKey('MachineGroup', models.CASCADE, null=False, blank=False, verbose_name='Группа оборудования')

    class Meta:
        db_table = 'MachineType'
        verbose_name = 'Тип оборудования'
        verbose_name_plural = 'Типы оборудования'

    def __str__(self):
        return f'{self.name}'