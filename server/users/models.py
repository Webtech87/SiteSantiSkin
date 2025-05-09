from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import PermissionsMixin, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser, PermissionsMixin):
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    accepted_terms = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password','phone','axcepted_terms']

    def __str__(self):
        return self.get_full_name()
