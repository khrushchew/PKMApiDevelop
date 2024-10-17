from django.db import models
from PKMApi.yandex_s3_storage import ClientImgStorage


class User(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Имя')
    surname = models.CharField(max_length=255, null=False, blank=False, verbose_name='Фамилия')
    second_name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Отчество')
    profile_picture = models.FileField(storage=ClientImgStorage(), blank=True, null=True, verbose_name='Фотография')

    login = models.CharField(unique=True, max_length=100, null=False, blank=False, verbose_name='Логин')
    password = models.CharField(max_length=255, null=False, blank=False, verbose_name='Пароль')

    subdivision = models.ForeignKey('Subdivision', models.PROTECT, blank=True, null=True, verbose_name='Подразделение')
    position = models.CharField(max_length=255, null=True, blank=True, verbose_name='Должность')

    role = models.ForeignKey('Role', models.SET_NULL, null=True, blank=True, verbose_name='Роль')

    is_activated = models.BooleanField(default=False, blank=True, null=True, verbose_name='Подтверждённый')

    class Meta:
        db_table = 'User'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    
    def __str__(self):
        return f"{self.login}"