from rest_framework import serializers
from notes.apps.tasks.models import Task, Comment


class Tasks(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'created_by', 'asigned_to', 'status', 'percentage')


class TaskStatus(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'status', 'percentage')


class Comments(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'text')
