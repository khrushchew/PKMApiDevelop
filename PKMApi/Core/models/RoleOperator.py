from django.db import models


class RoleOperator(models.Model):
    role_name = models.ForeignKey('Role', models.PROTECT, null=False, blank=False, verbose_name='Название роли')
    user = models.ForeignKey('User', models.PROTECT, null=False, blank=False, verbose_name='Пользователь')
    area = models.ForeignKey('Area', models.PROTECT, null=True, blank=True, verbose_name='Площадка')

    

    class Meta:
        db_table = 'RoleOperator'
        verbose_name = 'Роль оператора'
        verbose_name_plural = 'Роль операторов'

    
    def __str__(self):
        return f"{self.role_name}"