from django.db import models


class About(models.Model):
    version = models.CharField(default='1.0.0', null=False, blank=False, verbose_name='Версия приложения')
    upd = models.DateField(null=False, blank=False, verbose_name='Обновление от')

    address = models.CharField(null=False, blank=False, verbose_name='Адрес')

    info = models.CharField(default='0', null=False, blank=False, verbose_name='Информация')

    instruction = models.CharField(default='0', null=False, blank=False, verbose_name='Инструкция по эксплуатации')
