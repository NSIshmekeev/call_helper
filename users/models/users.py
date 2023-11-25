from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from users.models.managers import CustomUserManager


class User(AbstractUser):
    username = models.CharField('Никнейм', max_length=64,
                                unique=True, null=True, blank=True)
    phone_number = PhoneNumberField('Телефон', unique=True, null=True,
                                    blank=True)
    email = models.EmailField('Почта', unique=True, max_length=254, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

