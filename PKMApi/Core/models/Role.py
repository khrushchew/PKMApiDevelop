from django.db import models


class Role(models.Model):
    name = models.CharField(unique= True, max_length=255, null=False, blank=False, verbose_name='Название должности')

    class Meta:
        db_table = 'Role'
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    
    def __str__(self):
        return f"{self.name}"
