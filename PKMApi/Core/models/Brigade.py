from django.db import models


class Brigade(models.Model):
    code = models.CharField(max_length=100, null=False, blank=False, verbose_name='Код бригады')
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Название бригады')
    area = models.ForeignKey("Area", models.CASCADE, null=False, blank=False, verbose_name='Участок')

    class Model:
        db_table = 'Brigade'
        verbose_name = 'Бригада'
        verbose_name_plural = 'Бригады'

    def __str__(self):
        return f'{self.name}'