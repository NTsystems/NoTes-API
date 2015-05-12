from django.db import models
from django.conf import settings


class Notebook(models.Model):
    name = models.CharField(max_length=30, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        """Return the name of notebook"""
        return self.name


class Note(models.Model):
    """This class shows how the note appears"""
    title = models.CharField(max_length=30)
    contents = models.TextField(blank=True)
    date_of_create = models.DateField(verbose_name='creation date', auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    notebook = models.ForeignKey(Notebook)

    def __str__(self):
        """Return the title of note"""
        return self.title
