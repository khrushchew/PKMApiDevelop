from django.db import models


class Order(models.Model):
    number = models.CharField(unique=True, max_length=100, null=False, blank=False)
    date_receipt = models.DateField(null=False, blank=False)
    required_completion_date = models.DateField(null=True, blank=True)
    priority = models.IntegerField(blank=False, null=False)
    order_status = models.ForeignKey('Orderstatus', models.SET_NULL, blank=True, null=True)
    calculated_completion_date = models.DateField(blank=True, null=True)
    actual_completion_date = models.DateField(blank=True, null=True)
    company = models.ForeignKey('Company', models.CASCADE, blank=False, null=False)
    customer = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        db_table = 'Order'