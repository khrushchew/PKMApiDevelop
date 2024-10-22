from django.db import models

class BrigadeMachineUser(models.Model):
    machine = models.ForeignKey('Machine', models.SET_NULL, null=True, blank=True, verbose_name='Оборудование')
    user = models.ForeignKey('User', models.SET_NULL, null=True, blank=True, verbose_name='Работник')
    brigade = models.ForeignKey('Brigade', models.CASCADE, null=False, blank=False, verbose_name='Бригада')

    class Meta:
        db_table = 'BrigadeMachineUser'
        verbose_name = 'Рспределение бригады'
        verbose_name_plural = 'Распределение бригад'

    def __str__(self):
        return f'{self.machine}-{self.user}'