from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import EmailUserManager


# AbstractUser - используем тогда, когда хотим добавить новые поля к встроенному Джанго Юзеру
# class ExtendedUser(AbstractUser):
#     iin = models.CharField(max_length=12, unique=True)


class EmailUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = EmailUserManager()
