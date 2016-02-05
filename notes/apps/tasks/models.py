from django.db import models
from django.conf import settings
from audit_log.models.fields import CreatingUserField


class Task(models.Model):
    NEW = 1
    IN_PROGRESS = 2
    DONE = 3
    CLOSED = 4

    STATUS_CHOICES = (
        (NEW, 'New'),
        (IN_PROGRESS, 'In_progress'),
        (DONE, 'Done'),
        (CLOSED, 'Closed'),
    )

    name = models.CharField(max_length=30, unique=True)
    asigned_to = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_by = CreatingUserField(related_name="created_by")
    description = models.TextField(blank=True)
    percentage = models.FloatField(default=0.0)
    status = models.IntegerField(choices=STATUS_CHOICES, default=NEW)

    def __str__(self):
        return self.name


class Comment(models.Model):
    task = models.ForeignKey(Task)
    text = models.TextField(blank=True)
