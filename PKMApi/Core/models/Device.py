from django.db import models


class Device(models.Model):
    
    company = models.ForeignKey('Company', models.CASCADE, null=False, blank=False, verbose_name='Компания')
    code = models.CharField(max_length=100, null=False, blank=False, verbose_name='Код устройства') 
    counter = models.BigIntegerField(default=0, null=True, blank=True, verbose_name='Количество устройств')
    
    class Meta:
        db_table = 'Device'
        verbose_name = 'Устройство'
        verbose_name_plural = 'Устройства'

    def __str__(self):
        return f'{self.company} - {self.code}'
