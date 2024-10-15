from django.db import models


class Area(models.Model):
    name = models.CharField(max_length=255, null=False, blank = False, verbose_name='Название участка')
    indent = models.IntegerField(default=0, blank=False, null=False, verbose_name='Идентификатор')
    department = models.ForeignKey('Department', models.CASCADE, blank=False, null=False, verbose_name='Название цеха')

    class Meta:
        db_table = 'Area'
        verbose_name = 'Участок'
        verbose_name_plural = 'Участки'

    def __str__(self):
        return f"{self.name}"
