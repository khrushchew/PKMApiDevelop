from django.db import models


class Platform(models.Model):
    indent = models.PositiveIntegerField(default=0, null=False, blank=False, verbose_name="Идентификатор")
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Название площадки")
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name="Адрес площадки")
    company = models.ForeignKey('Company', models.CASCADE, null=False, blank=False, verbose_name="Название компании")

    class Meta:
        db_table = 'Platform'
        verbose_name = "Площадка"
        verbose_name_plural = "Площадки"


    def __str__(self):
        return f"{self.name}"