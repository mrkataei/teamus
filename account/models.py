from django.db import models
from django.contrib.auth.models import AbstractUser


class Member(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
