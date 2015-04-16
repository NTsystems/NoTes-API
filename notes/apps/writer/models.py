from django.db import models
#import datetime


class Notebook(models.Model):
    name = models.CharField(max_length=30, unique=True)
    user = models.ForeignKey(User)
    def __str__(self):
        return self.name

class Note(models.Model):
    title = models.CharField(max_length=30)
    contents = models.TextField(blank = True)
    date_of_create = models.DateField.auto_now_add('creation date')
    last_modified = models.DateTimeField.auto_now()
    notebook = models.ForeignKey(Notebook)
    def __str__(self):
        return self.title
# Create your models here.
