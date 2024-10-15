from django.db import models


class Field(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Название площадки")
    company = models.ForeignKey('Company', models.CASCADE, null=False, blank=False, verbose_name="Название компании")

    class Meta:
        db_table = 'Field'
        verbose_name = "Площадка"
        verbose_name_plural = "Площадки"


    def __str__(self):
        return f"{self.name}"