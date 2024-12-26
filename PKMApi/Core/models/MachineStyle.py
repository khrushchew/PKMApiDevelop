from django.db import models


class MachineStyle(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название')
    company = models.ForeignKey('Company', models.CASCADE, null=False, blank=False, verbose_name='Компания')

    class Meta:
        db_table = 'MachineStyle'
        verbose_name = 'Вид оборудования'
        verbose_name_plural = 'Виды оборудования'

    def __str__(self):
        return f"{self.name}"
