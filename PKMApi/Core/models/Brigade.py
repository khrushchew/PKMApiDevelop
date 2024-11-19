from django.db import models


class Brigade(models.Model):
    company = models.ForeignKey('Company', models.CASCADE, null=False, blank=False, verbose_name='Компания')
    code = models.CharField(max_length=100, null=False, blank=False, verbose_name='Код бригады')
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Название бригады')
    area = models.ForeignKey("Area", models.CASCADE, null=False, blank=False, verbose_name='Участок')
    shift_mode = models.ForeignKey('ShiftMode', models.PROTECT, null=True, blank=True, verbose_name='Режим сменности')

    class Meta:
        db_table = 'Brigade'
        verbose_name = 'Бригада'
        verbose_name_plural = 'Бригады'

    def __str__(self):
        return f'{self.name}'