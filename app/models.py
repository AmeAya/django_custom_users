from django.db import models
from django.contrib.auth.models import AbstractUser


# AbstractUser - используем тогда, когда хотим добавить новые поля к встроенному Джанго Юзеру
class ExtendedUser(AbstractUser):
    iin = models.CharField(max_length=12, unique=True)
