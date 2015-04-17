from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    password = models.CharField(_('password'), max_length=50)
    e_mail = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'e_mail'
    REQUIRED_FIELDS = []

    def get_username(self):
        """ Returns the value of the field nominated by USERNAME_FIELD."""
        return getattr(self, self.USERNAME_FIELD)

    def is_authenticated(self):
        """Return True. This is a way to tell if the user has been authenticated."""
        return True

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        def setter(self, raw_password):
            self.set_password(raw_password)
            self.save(update_fields=["password"])
        return check_password(raw_password, self.password, setter)

    def set_unusable_password(self):
        self.password = make_password(None)


    class Meta:
        permission = ('change_password',)


    def __str__(self):
        return self.username


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
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