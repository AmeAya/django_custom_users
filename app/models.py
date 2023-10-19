from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import EmailUserManager


# AbstractUser - используем тогда, когда хотим добавить новые поля к встроенному Джанго Юзеру
# class ExtendedUser(AbstractUser):
#     iin = models.CharField(max_length=12, unique=True)


# class EmailUser(AbstractUser):
#     username = None
#     email = models.EmailField(unique=True)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#     objects = EmailUserManager()


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = EmailUserManager()  # object - Это набор правил, как создавать, удалять, обновлять объекты этой модели
