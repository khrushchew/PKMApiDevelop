from django.db.models.signals import post_save, post_delete

from django.dispatch import receiver

from .models.Area import Area
from .models.Machine import Machine
from .models.User import User
from .models.Department import Department


@receiver(post_save, sender=Area)
@receiver(post_delete, sender=Area)
@receiver(post_save, sender=Machine)
@receiver(post_delete, sender=Machine)
def update_department_quantity(sender, instance, **kwargs):
    instance.department.save()
