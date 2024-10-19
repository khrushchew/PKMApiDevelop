from django.db import models


class MachineName(models.Model):
    inv_number = models.PositiveIntegerField(null=False, blank=False, verbose_name='Инвентарный номер')
    machine_code = models.CharField(max_length=100, null=False, blank=False ,verbose_name='Модель')
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название')
    surname = models.CharField(max_length=255, null=False, blank=False, verbose_name='Дополнительное название')
    type = models.ForeignKey('MachineType', models.CASCADE, null=False, blank=False, verbose_name='Тип оборудования')
    machine_control_method = models.ForeignKey('MachineControlMethod', models.SET_NULL , null=True, blank=True, verbose_name='Способ управления оборудованием')

    class Meta:
        db_table = 'MachineName'
        verbose_name = 'Модель оборудования'
        verbose_name_plural = 'Модели оборудования'

    def __str__(self):
        return f'{self.name}'