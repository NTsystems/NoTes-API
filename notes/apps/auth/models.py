from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class User(AbstractBaseUser):
    e_mail = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'e_mail'
    REQUIRED_FIELDS = []


    class Meta:
        permission = ('change_password',)


    def __str__(self):
        return self.username

class UserManager(BaseUserManager):
    def create_user(self, e_mail, password=None):
         """
        Creates and saves a User with the given email and password.
        """
        if not e_mail:
            reise ValueError('Users must have an email address')

        user = self.model(e_mail=self.normalize_email(e_mail),)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, e_mail, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(e_mail, password=password)
        user.is_admin = True
        user.save()
        return user


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField(blank=True)
    place = models.CharField(max_length=50, blank=True)
    state = models.CharField(verbose_name='country', max_length=50, blank=True)

    class Meta:
        permission = ('change_date_of_birth', 'change_place', 'change_state',)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name