from django.db import models
from PKMApi.yandex_s3_storage import ClientImgStorage

class Machine(models.Model):
    invent_number = models.ForeignKey('MachineName', models.CASCADE, blank=False, null=False, verbose_name='Инвентарный номер')

    ratio = models.PositiveIntegerField(default = 0, blank=False, null=False, verbose_name='Коэффициент многостачности')
    tariff = models.PositiveIntegerField(default = 0, blank=False, null=False, verbose_name='Сдельный тариф')
 
    area = models.ForeignKey('Area', models.CASCADE, null=False, blank=False, verbose_name='Участок')

    img = models.FileField(storage=ClientImgStorage(), blank=True, null=True, verbose_name='Фотография')
    
    class Meta:
        db_table = 'Machine'

    def __str__(self):
        return f'{self.invent_number}'