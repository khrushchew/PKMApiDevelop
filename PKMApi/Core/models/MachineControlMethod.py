from django.db import models


class MachineControlMethod(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название')

    class Meta:
        db_table = 'MachineControlMethod'
        verbose_name = 'Способ управления оборудованием'
        verbose_name_plural = 'Способы управления оборудованием'

    def __str__(self):
        return f'{self.name}'
    