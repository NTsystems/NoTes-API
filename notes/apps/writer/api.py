from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from notes.apps.writer.models import Note, Notebook
from notes.apps.writer.resources import NotebookSerializer, NoteSerializer
from django.http import Http404



class NotebookList(APIView):

    def get(self, request, format=None):
        """List all notebooks"""
        notebooks = Notebook.objects.all()
        serializer = NotebookSerializer(notebooks, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, format = None):
        """Create notebook"""
        serializer = NotebookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class NotebookDetail(APIView):

    def get_objects(self, id):

        try:
            return Notebook.objects.get(pk = id)
        except Notebook.DoesNotExist:
            raise Http404

    def get(self, request, id, format= None):
        notebook = self.get_objects(id)
        serialiazer = NotebookSerializer(notebook)
        return Response(serialiazer.data, status = status.HTTP_200_OK)


    def delete(self, request, id, format= None):
        """Delete notebook"""
        notebook = self.get_objects(id)
        notebook.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


class NoteList(APIView):

    def get(self, request, format = None):
        """List all notes from notebook ID"""
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, format = None):
        """Create note """
        serializer = NoteSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class NoteDetail(APIView):

    def get_object(self, pk):

        try:
            return Note.objects.get(pk = pk)
        except Note.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        """Update note"""
        note = self.get_object(pk)
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):
        """Delete note"""
        note = self.get_object(pk)
        note.delete()
        return  Response(status = status.HTTP_204_NO_CONTENT)









