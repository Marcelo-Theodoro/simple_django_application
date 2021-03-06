from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from .constants import COUNTRIES


class User(AbstractUser):
    name = models.CharField(max_length=128)
    country = models.CharField(max_length=2, choices=COUNTRIES)


class Business(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
