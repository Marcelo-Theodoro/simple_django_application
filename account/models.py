from django.db import models, transaction
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from .constants import COUNTRIES


class User(AbstractUser):
    name = models.CharField(max_length=128)
    country = models.CharField(max_length=2, choices=COUNTRIES)

    @transaction.atomic
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.business.exists():
            Business.objects.create(user=self, is_active=True)


class Business(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="business", on_delete=models.CASCADE
    )
    is_active = models.BooleanField(default=False)
