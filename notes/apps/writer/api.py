from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import authentication, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from notes.apps.writer.models import Note, Notebook
from notes.apps.writer.resources import Notebooks, Notes


class NotebookList(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)

    def get(self, request):
        """Retrieves all notebooks user has created.
        ---
        request_serializer: notes.apps.writer.resources.Notebooks

        responseMessages:
            - code: 200
              message: Retrieval succeeded.
            - code: 404
              message: No notebooks found.
            - code: 401
              message: Unauthorized.
        """
        notebooks = get_list_or_404(Notebook)
        serializer = Notebooks(notebooks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Creates an empty notebook.
        ---
        parameters:
            - name: name
              description: Unique notebook name.
              required: true
              type: string
              paramType: form

        responseMessages:
            - code: 201
              message: Notebook created.
            - code: 400
              message: Invalid or missing data provided.
            - code: 401
              message: Unauthorized.
        """
        serializer = Notebooks(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NotebookDetail(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)

    def get(self, request, notebook_id):
        """Retrieves particular notebook.
        ---
        request_serializer: notes.apps.writer.resources.Notebooks

        responseMessages:
            - code: 200
              message: Retrieval succeeded.
            - code: 404
              message: Notebook with given id does not exist.
            - code: 401
              message: Unauthorized.
        """
        notebook = get_object_or_404(Notebook, id=notebook_id, user=request.user)
        serializer = Notebooks(notebook)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, notebook_id):
        """Removes notebook.
        ---
        responseMessages:
            - code: 204
              message: Notebook has been removed.
        """
        Notebook.objects.filter(id=notebook_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NoteList(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)

    def get(self, request, notebook_id):
        """Retrieves all notes from a particular notebook.
        ---
        request_serializer: notes.apps.writer.resources.Notes

        responseMessages:
            - code: 200
              message: Retrieval succeeded.
            - code: 404
              message: Notebook empty or non-existent.
        """
        notes = get_list_or_404(Note, notebook__id=notebook_id)
        serializer = Notes(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, notebook_id):
        """Adds new note to the specified notebook.
        ---
        parameters:
            - name: title
              description: Note title.
              required: true
              type: string
              paramType: form
            - name: contents
              description: Note content.
              required: false
              type: string
              paramType: form

        responseMessages:
            - code: 201
              message: Note has been created.
            - code: 400
              message: Invalid or missing data supplied.
            - code: 404
              message: Required notebook does not exist.
        """
        notebook = get_object_or_404(Notebook, id=notebook_id)
        serializer = Notes(data=request.data)
        if serializer.is_valid():
            serializer.save(notebook=notebook)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteDetail(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)

    def get(self, request, notebook_id, note_id):
        """Retrieves content of a particular note.
        ---
        request_serializer: notes.apps.writer.resources.Notes

        responseMessages:
            - code: 200
              message: Retrieval succeeded.
            - code: 404
              message: Non-existent resource required.

        """
        note = get_object_or_404(Note, id=note_id, notebook__id=notebook_id)
        serializer = Notes(note)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, notebook_id, note_id):
        """Updates a particular note.
        ---
        request_serializer: notes.apps.writer.resources.Notes

        responseMessages:
            - code: 204
              message: Note has been updated.
            - code: 400
              message: Invalid or missing data supplied.
            - code: 404
              message: Non-existent resource required.
        """
        note = get_object_or_404(Note, id=note_id, notebook__id=notebook_id)
        serializer = Notes(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, notebook_id, note_id):
        """Removes a particular note.
        ---
        responseMessages:
            - code: 204
              message: Note has been removed.
        """
        Note.objects.filter(id=note_id, notebook__id=notebook_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
