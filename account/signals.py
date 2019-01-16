from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Business


@receiver(post_save, sender=User)
def criar_business(sender, instance, created=False, **kwargs):
    if created:
        Business.objects.create(user=instance, is_active=True)
