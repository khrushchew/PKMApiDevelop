from django.db import models
from django.utils import timezone

class MonthlyWorkLog(models.Model):
    date = models.DateField()
    day_of_week = models.CharField(max_length=10)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    work_hours = models.ForeignKey()

    class Meta:
        unique_together = ('date', 'user')
        ordering = ['date']

    def __str__(self):
        return f"{self.employee} - {self.date}: {self.work_hours} часов"
