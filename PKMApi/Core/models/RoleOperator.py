from django.db import models


class RoleOperator(models.Model):
    role_name = models.ForeignKey('Role', models.PROTECT, null=False, blank=False, verbose_name='Название роли')
    user = models.ForeignKey('User', models.PROTECT, null=False, blank=False, verbose_name='Пользователь')
    platform = models.ForeignKey('Platform', models.PROTECT, null=True, blank=True, verbose_name='Площадка')
    department = models.ForeignKey('Department', models.PROTECT, null=True, blank=True, verbose_name='Цех')
    area = models.ForeignKey('Area', models.PROTECT, null=True, blank=True, verbose_name='Площадка')

    class Meta:
        db_table = 'RoleOperator'
        verbose_name = 'Роль оператора'
        verbose_name_plural = 'Роли оператора'

    
    def __str__(self):
        return f"{self.role_name}"