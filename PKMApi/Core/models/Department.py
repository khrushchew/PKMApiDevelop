from django.db import models

from .Area import Area
from .Machine import Machine
from .User import User


class Department(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Название цеха')
    platform = models.ForeignKey('Platform', models.CASCADE, blank=False, null=False, verbose_name='Название площадки')
    main_user = models.ForeignKey('User', models.SET_NULL, blank=True, null=True, verbose_name='Начальник цеха')

    class Meta:
        db_table = 'Department'
        verbose_name = 'Цех'
        verbose_name_plural = 'Цеха'

    
    def __str__(self):
        return f"{self.name}"