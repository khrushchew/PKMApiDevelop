from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Название роли")
    company = models.ForeignKey('Company', models.CASCADE, null=False, blank=False, verbose_name="Компания")

    class Meta:
        db_table = 'Role'
        verbose_name = 'Роль'
        verbose_name_plural = 'Роль'

    def __str__(self):
        return f"{self.name}"
