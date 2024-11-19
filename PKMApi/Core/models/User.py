from django.db import models
from django.contrib.auth.models import AbstractUser
from PKMApi.yandex_s3_storage import ClientImgStorage


class User(AbstractUser):
    company = models.ForeignKey('Company', models.CASCADE, null=True, blank=True, verbose_name='Компания')

    surname = models.CharField(max_length=255, null=True, blank=True, verbose_name='Отчество')

    profile_picture = models.FileField(storage=ClientImgStorage(), blank=True, null=True, verbose_name='Фотография')

    password = models.CharField(max_length=255, null=True, blank=False, verbose_name='Пароль')

    subdivision = models.ForeignKey('Subdivision', models.SET_NULL, blank=True, null=True, verbose_name='Подразделение')
    position = models.CharField(max_length=255, null=True, blank=True, verbose_name='Должность')

    token = models.CharField(null=True, blank=True, verbose_name='Токен')

    def __str__(self):
        return f"{self.username}"
    