from rest_framework import serializers
from notes.apps.writer.models import Notebook, Note

class NotebookSerializer(serializers.ModelSerializer):

    # def create(self, validated_data):
    #     notebook = Notebook.objects.create(user = self.context['request'].user, **validated_data)
    #     return notebook


    class Meta:
        model = Notebook
        fields = ('id', 'name')



class NoteSerializer(serializers.ModelSerializer):

    # def create(self, validated_data):
    #     note = Note.objects.create(notebook = self.context['notebook'], **validated_data)
    #     return note

    class Meta:
        model = Note
        fields = ('id', 'title', 'contents')