from django.db import models


class Shift(models.Model):
    brigade = models.ForeignKey('Brigade', models.CASCADE, null=False, blank=False, verbose_name='Бригада')
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название')

    class Meta:
        db_table = 'Shift'
        verbose_name = 'Смена'
        verbose_name_plural = 'Смены'

    def __str__(self):
        return f'{self.company} - {self.name}'
