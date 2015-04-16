from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        permission = ('change_password',)


    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField(blank=True)
    e_mail = models.EmailField(verbose_name='e-mail',blank=True)
    place = models.CharField(max_length=50, blank=True)
    state = models.CharField(verbose_name='country', max_length=50, blank=True)

    class Meta:
        permission = ('change_date_of_birth', 'change_place', 'change_state',)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name