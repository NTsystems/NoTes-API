from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from notes.apps.writer.models import Note, Notebook
from notes.apps.writer.resources import NotebookSerializer, NoteSerializer
from django.shortcuts import get_object_or_404


class NotebookList(APIView):
    """Create notebook or retrieve all notebooks"""

    def get(self, request):
        """List all notebooks"""

        notebooks = Notebook.objects.all()
        if not notebooks:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = NotebookSerializer(notebooks, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)


    def post(self, request):
        """Create notebook"""

        serializer = NotebookSerializer(data = request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



class NotebookDetail(APIView):
    """Read notebook and delete notebook with notebook_id """

    def get(self, request, notebook_id):
        """Retrieve notebook with notebook_id"""

        notebook = get_object_or_404(Notebook, id = notebook_id)
        serializer = NotebookSerializer(notebook)
        return Response(serializer.data, status = status.HTTP_200_OK)


    def delete(self, request, notebook_id):
        """Delete notebook with notebook_id"""

        notebook = get_object_or_404(Notebook, id = notebook_id)
        notebook.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)



class NoteList(APIView):
    """List all notes from notebook with notebook_id or create new note"""

    def get(self, request, notebook_id):
        """List all notes from notebook_id"""

        get_object_or_404(Notebook, id = notebook_id)
        notes = Note.objects.all().filter(notebook_id = notebook_id)
        # if not notes:
        #     return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)


    def post(self, request, notebook_id):
        """Create note in notebook with notebook_id  """

        notebook = Notebook.objects.get(id = notebook_id)
        serializer = NoteSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(notebook = notebook)
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



class NoteDetail(APIView):
    """Update note or delete note from notebook_id"""

    def get(self, request, notebook_id, id):
        """Read note with note_id"""
        get_object_or_404(Notebook, id = notebook_id)
        note = Note.objects.all().filter(notebook_id = notebook_id)
        note = get_object_or_404(Note, pk = id)
        serializer = NoteSerializer(note)
        return Response(serializer.data, status = status.HTTP_200_OK)


    def put(self, request, notebook_id, id):
        """Update note"""
        get_object_or_404(Notebook, id = notebook_id)
        note = Note.objects.all().filter(notebook_id = notebook_id)
        note = get_object_or_404(Note, pk = id)
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id, notebook_id):
        """Delete note"""

        get_object_or_404(Notebook, id = notebook_id)
        note = Note.objects.all().filter(notebook_id = notebook_id)
        note = get_object_or_404(Note, pk = id)
        note.delete()
        return  Response(status = status.HTTP_204_NO_CONTENT)









