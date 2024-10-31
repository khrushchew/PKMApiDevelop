from django.db import models
from PKMApi.yandex_s3_storage import ClientImgStorage

class MachineName(models.Model):
    inv_number = models.PositiveIntegerField(null=False, blank=False, verbose_name='Инвентарный номер')
    machine_code = models.CharField(max_length=100, null=False, blank=False ,verbose_name='Модель')
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название')
    surname = models.CharField(max_length=255, null=False, blank=False, verbose_name='Дополнительное название')
    img = models.FileField(storage=ClientImgStorage(), blank=True, null=True, verbose_name='Фотография')

    company = models.ForeignKey('Company', models.CASCADE, null=False, blank=False, verbose_name='Компания')
    type = models.ForeignKey('MachineType', models.SET_NULL, null=True, blank=True, verbose_name='Тип оборудования')
    machine_control_method = models.ForeignKey('MachineControlMethod', models.SET_NULL , null=True, blank=True, verbose_name='Способ управления оборудованием')
    
    ratio = models.PositiveIntegerField(default=0, null=True, blank=True, verbose_name='Коэффициент многостаночности')
    tarife = models.PositiveIntegerField(default=0, null=True, blank=True, verbose_name='Сдельный тариф')

    area = models.ForeignKey('Area', models.PROTECT, null=False, blank=False, verbose_name='Участок')
    
    work_time = models.CharField(null=True, blank=True, verbose_name='Время работы')
    
    brigade = models.ForeignKey('Brigade', models.SET_NULL, null=True, blank=True, verbose_name='Бригада')

    class Meta:
        db_table = 'MachineName'
        verbose_name = 'Карточка оборудования'
        verbose_name_plural = 'Карточки оборудования'

    def __str__(self):
        return f'{self.name}'
