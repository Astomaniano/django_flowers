from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Phone Number")

    def __str__(self):
        return self.username