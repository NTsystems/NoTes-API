from django.contrib import admin
from notes.apps.writer.models import Notebook, Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'last_modified', 'date_of_create')
    search_fields = ('title',)


admin.site.register(Notebook)
admin.site.register(Note, NoteAdmin)

