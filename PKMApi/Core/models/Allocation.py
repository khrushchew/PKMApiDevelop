from django.db import models
from django.contrib.auth.models import Group

from Core.models.User import User


class Allocation(models.Model):
    user = models.ForeignKey(User, models.CASCADE, blank=False, null=False, verbose_name='Пользователь')
    group = models.ForeignKey(Group, models.CASCADE, blank=False, null=False, verbose_name='Группа')

    platform = models.ForeignKey('Platform', models.CASCADE, blank=False, null=False, verbose_name='Площадка')
    department = models.ManyToManyField('Department', verbose_name='Цеха')
    area = models.ManyToManyField('Area', verbose_name='Участки')

    brigade = models.ForeignKey('Brigade', models.SET_NULL, null=True, blank=True, verbose_name='Бригада')
    shift = models.ForeignKey('Shift', models.SET_NULL, null=True, blank=True, verbose_name='Смена')

    class Meta:
        db_table = 'Allocation'
