from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    some_model_field = models.TextField()

    objects = BaseUserManager()

    USERNAME_FIELD = "email"
