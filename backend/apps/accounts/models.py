from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import random

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, phone, email=None, password=None, **extra):
        if not phone:
            raise ValueError("Phone number is required")
        email = self.normalize_email(email)
        user = self.model(phone=phone, email=email, **extra)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, phone, email=None, password=None, **extra):
        extra.setdefault('is_staff', True)
        extra.setdefault('is_superuser', True)
        return self.create_user(phone, email, password, **extra)
    
class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=11, unique=True)
    email = models.EmailField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone
    
class PanelOTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='otps')
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_used = models.BooleanField(default=False)

    @classmethod
    def generate_otp(cls, user):
        code = f'{random.randint(0, 999999):06d}'
        return cls.objects.create(user=user, code=code, expires_at=timezone.now() + timezone.timedelta(minutes=10))
    
    def __str__(self):
        return f"{self.user.phone} - {self.code}"