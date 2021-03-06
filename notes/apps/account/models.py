import logging

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token

logger = logging.getLogger(__name__)


class UserManager(BaseUserManager):
    def _create_user(self, e_mail, password, is_staff, is_superuser, **extra_fields):
        """Creates and saves a User with the given email and password."""
        now = timezone.now()
        if not e_mail:
            raise ValueError('Users must have an email address')
        e_mail = self.normalize_email(e_mail)
        user = self.model(e_mail=e_mail,
                          is_staff=is_staff,
                          is_active=False,
                          is_superuser=is_superuser,
                          last_login=now,
                          **extra_fields)

        user.set_password(password)
        user.save()
        return user

    def create_user(self, e_mail=None, password=None, **extra_fields):
        return self._create_user(e_mail, password, False, False,
                                 **extra_fields)

    def create_superuser(self, e_mail, password, **extra_fields):
        return self._create_user(e_mail, password, True, True,
                                 **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    e_mail = models.EmailField(unique=True)
    
    try:
        activation_key = models.CharField(max_length=40, blank=True, default=" ")
        key_expires = models.DateTimeField(default=timezone.now())
    except ValueError as v:
        logger.warn("Problem with activation_key and key_expires values.")

    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'e_mail'
    REQUIRED_FIELDS = []

    def get_short_name(self):
        return self.e_mail


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="profile")
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    place = models.CharField(max_length=50, blank=True)
    state = models.CharField(verbose_name='country', max_length=50, blank=True)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name
