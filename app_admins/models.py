from django.contrib.auth.models import AbstractUser
from django.db import models


class AdminsUser(AbstractUser):
    email = models.EmailField()
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'admins'
        verbose_name_plural = 'admins'