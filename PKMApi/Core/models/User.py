from django.db import models
from PKMApi.yandex_s3_storage import ClientImgStorage


class User(models.Model):
    login = models.CharField(unique=True, max_length=100, null=False, blank=False, verbose_name='Логин')
    password = models.CharField(max_length=255, null=False, blank=False, verbose_name='Пароль')
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='ФИО')
    subdivision = models.ForeignKey('Subdivision', models.SET_NULL, blank=True, null=True, verbose_name='Подразделение')
    role = models.ForeignKey('Role', models.SET_NULL, blank=True, null=True, verbose_name='Должность')
    is_activated = models.BooleanField(default=False, blank=True, null=True, verbose_name='Подтверждённый')
    profile_picture = models.FileField(storage=ClientImgStorage(), blank=True, null=True, verbose_name='Фотография')


    class Meta:
        db_table = 'User'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    
    def __str__(self):
        return f"{self.login}"