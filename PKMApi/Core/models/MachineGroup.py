from django.db import models


class MachineGroup(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название')
    style = models.ForeignKey('MachineStyle', models.CASCADE, null=False, blank=False, verbose_name='Вид оборудования')

    class Meta:
        db_table = 'MachineGroup'
        verbose_name = 'Группа оборудования'
        verbose_name_plural = 'Группы оборудования'

    def __str__(self):
        return f'{self.name}'
