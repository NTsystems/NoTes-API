from django.db import models
from django.conf import settings



class Notebook(models.Model):

    name = models.CharField(max_length=30, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        """Return the name of notebook"""
        return self.name


class Note(models.Model):
    """class
    """

    title = models.CharField(max_length=30)
    contents = models.TextField(blank = True)
    date_of_create = models.DateField.auto_now_add('creation date')
    last_modified = models.DateTimeField.auto_now()
    notebook = models.ForeignKey(Notebook)

    def __str__(self):
        """Return the title of note"""
        return self.title
# Create your models here.
