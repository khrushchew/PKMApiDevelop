from django.db import models

class Department(models.Model):
    indent = models.PositiveIntegerField(default=0, null=False, blank=False, verbose_name="Идентификатор")
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Название цеха')
    platform = models.ForeignKey('Platform', models.CASCADE, blank=False, null=False, verbose_name='Название площадки')
    main_user = models.CharField(blank=False, null=False, verbose_name='Начальник цеха')

    class Meta:
        db_table = 'Department'
        verbose_name = 'Цех'
        verbose_name_plural = 'Цеха'

    
    def __str__(self):
        return f"{self.name}"