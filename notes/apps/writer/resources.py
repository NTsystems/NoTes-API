#from django.forms import widgets
from rest_framework import serializers
from notes.apps.writer.models import Notebook, Note

class NotebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notebook
        fields = ('id', 'name')


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title', 'contents')