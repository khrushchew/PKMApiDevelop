from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Название компании')
    code = models.CharField(max_length=100, null=False, blank=False, verbose_name='Код компании')
    is_paid = models.BooleanField(default=False, blank=False, verbose_name='Оплата')
    paid_machines_quantity = models.IntegerField(default=0, null=True, blank=True, verbose_name='Количество оплаченных машин')
    date_of_start = models.DateField(null=True, blank=True, verbose_name='Дата начала подписки')
    date_of_end = models.DateField(null=True, blank=True, verbose_name='Дата окончания подписки')
    is_testdrive = models.BooleanField(default=True, verbose_name='Тестовый период')
    number_of_support_staff = models.IntegerField(default=0, null=False, blank=False, verbose_name='Количество персонала')

    class Meta:
        db_table = 'Company'
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


    def __str__(self):
        return f"{self.name}"
