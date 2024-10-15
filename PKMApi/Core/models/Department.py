from django.db import models

from .Area import Area
from .Machine import Machine
from .User import User


class Department(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Название цеха')
    field = models.ForeignKey('Field', models.CASCADE, blank=False, null=False, verbose_name='Название площадки')
    indent = models.IntegerField(default=0, blank=False, null=False, verbose_name='Идентификатор')

    areas_quantity = models.PositiveIntegerField(default=0, null=False, blank=False, verbose_name='Количество участков')
    machines_quantity = models.PositiveIntegerField(default=0, null=False, blank=False, verbose_name='Количество машин')
    # stuff_quantity = models.PositiveIntegerField(default=0, null=False, blank=False, verbose_name='Количество персонала')

    def save(self, *args, **kwargs):
        self.areas_quantity = Area.objects.filter(department__field=self.field).count()
        self.machines_quantity = Machine.objects.filter(area__department__field=self.field).count()
        # self.stuff_quantity = User.objects.filter(subdivision__area__department__field=self.field).count()

        super().save(*args, **kwargs)


    class Meta:
        db_table = 'Department'
        verbose_name = 'Цех'
        verbose_name_plural = 'Цеха'

    
    def __str__(self):
        return f"{self.name}"