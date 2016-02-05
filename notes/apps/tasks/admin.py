from django.contrib import admin
from .models import Task, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')


admin.site.register(Task)
admin.site.register(Comment, CommentAdmin)
