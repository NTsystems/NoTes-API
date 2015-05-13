from rest_framework import serializers
from notes.apps.writer.models import Notebook, Note


class Notebooks(serializers.ModelSerializer):

    class Meta:
        model = Notebook
        fields = ('id', 'name')


class Notes(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ('id', 'title', 'contents')