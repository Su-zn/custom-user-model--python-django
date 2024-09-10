from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
import uuid




def uuid_default():
    return uuid.uuid4()


class CustomUser(AbstractBaseUser,PermissionsMixin):
    user_uuid = models.UUIDField(_("User Unique ID"), default=uuid_default, editable=False)
    email=models.EmailField(_("email address"),unique=True)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    mobile_no = models.CharField(_("mobile no."), max_length=15, null=True, blank=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now_add=True)
    oauth_token = models.CharField(max_length=255, blank=True, null=True)


    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    objects=CustomUserManager()

    def __str__(self):
        return self.email
