from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.forms import ValidationError

from users.managers import CustomUserManager


def validate_username(username):
    if len(username) < 8:
        raise ValidationError(
            "This username is too short. It must contain at least 8 character."
        )


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=32,
        unique=True,
        blank=False,
        default="",
        validators=[validate_username],
    )
    full_name = models.CharField(max_length=32, blank=False, default="")
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.username} {self.full_name}"
