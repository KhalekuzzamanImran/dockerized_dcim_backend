from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
import uuid

from account.mixins import contact_number_validator

# Create your models here.
class Role(models.Model):
    id = models.UUIDField(db_column='role_id', primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    key = models.CharField(max_length=64)

    def __str__(self):
        return self.key
    
    class Meta:
        db_table = 'role'


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users require an email field')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    id = models.UUIDField(db_column='user_id', primary_key=True, default=uuid.uuid4, editable=False)
    role = models.ForeignKey('account.Role', db_column='role_id', on_delete=models.SET_NULL, null=True, related_name='custom_users')
    full_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    contact_number = models.CharField(max_length=15, validators=[contact_number_validator])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'user'
        ordering = ['-date_joined']
    