from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from notes.apps.writer.models import Note, Notebook
from notes.apps.writer.resources import Notebooks, Notes


class NotebookList(APIView):
    """Create notebook or retrieve all notebooks

    Args:
        msg(str): Human readable string describing the APIView
    """
    def get(self, request):
        """List all notebooks

        Args:
            request (str): The first parameter
        returns:
            HTTP_200_OK if there are notebooks or
            HTT_404_NOT_FOUND if user don't have notebooks
        """
        notebooks = get_list_or_404(Notebook)
        serializer = Notebooks(notebooks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Create notebook

        Args:
            request (str): The first parameter
        Returns:
            HTTP_201_CREATED or HTTP_400_BAD_REQUEST
        """
        serializer = Notebooks(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NotebookDetail(APIView):
    """Read notebook and delete notebook with notebook_id """

    def get(self, request, notebook_id):
        """Retrieve notebook with notebook_id

        Args:
            request (str): The first parameter
            notebook_id (int): The second parameter.
        Returns:
            HTTP_200_OK if there is a notebook with notebook_id or
            HTTP_404_NOT_FOUND if there isn't notebook with notebook_id
        """
        notebook = get_object_or_404(Notebook, id=notebook_id)
        serializer = Notebooks(notebook)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, notebook_id):
        """Delete notebook with notebook_id

        Args:
            request (str): The first parameter
            notebook_id (int): The second parameter.
        Returns:
            HTTP_204_NO_CONTENT if notebook is deleted
        """
        Notebook.objects.filter(id=notebook_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NoteList(APIView):
    """List all notes from notebook with notebook_id or create new note"""

    def get(self, request, notebook_id):
        """List all notes from notebook with notebook_id

        Args:
            request (str): The first parameter
            notebook_id (int): The second parameter.
        Returns:
            HTTP_200_OK if there is notebook with notebook_id
            HTTP_404_NOT_FOUND if there isn't notebook with notebook_id
        """
        notes = get_list_or_404(Note, notebook__id=notebook_id)
        serializer = Notes(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, notebook_id):
        """Create note in notebook with notebook_id

        Args:
            request (str): The first parameter
            notebook_id (int): The second parameter.
        Returns:
            HTTP_201_CREATED or
            HTTP_400_BAD_REQUEST or
            HTTP_404_NOT_FOUND if there isn't notebook with notebook_id
        """
        notebook = get_object_or_404(Notebook, id=notebook_id)
        serializer = Notes(data=request.data)
        if serializer.is_valid():
            serializer.save(notebook=notebook)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteDetail(APIView):
    """Update note or delete note from notebook_id"""
    def get(self, request, notebook_id, note_id):
        """Read note with note_id

        Args:
            request (str): The first parameter
            notebook_id (int): The second parameter.
            note_id (int): The third parameter.Note id.
        Returns:
            HTTP_200_OK if there is note with id in notebook with notebook_id or
            HTTP_404_NOT_FOUND if there isn't notebook with notebook_id
            or there isn't note with id
        """
        note = get_object_or_404(Note, id=note_id, notebook__id=notebook_id)
        serializer = Notes(note)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, notebook_id, note_id):
        """Update note

        Args:
            request (str): The first parameter
            notebook_id (int): The second parameter.
            id (int): The third parameter.Note id.
        Returns:
            HTTP_204_NO_CONTENT if note with id is updated or
            HTTP_400_BAD_REQUEST or
            HTTP_404_NOT_FOUND if there isn't notebook with notebook_id
            or there isn't note with id
        """
        note = get_object_or_404(Note, id=note_id, notebook__id=notebook_id)
        serializer = Notes(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, notebook_id, note_id):
        """Delete note

        Args:
            request (str): The first paramneter
            notebook_id (int): The second parameter.
            id (int): The third parameter.Note id.
        Returns:
            HTTP_204_NO_CONTENT if note with id is deleted or
            HTTP_400_BAD_REQUEST or
            HTTP_404_NOT_FOUND if there isn't notebook with notebook_id
            or there isn't note with id
        """
        Note.objects.filter(id=note_id, notebook__id=notebook_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)









