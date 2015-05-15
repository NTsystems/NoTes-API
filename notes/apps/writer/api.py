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
        """List all notebooks
        ---
        request_serializer: notes.apps.writer.resources.Notebooks

        responseMessages:
            - code: 200
              message: List of all notebooks
            - code: 404
              message: Not found
            - code: 401
              message: Not authenticated
        """
        notebooks = get_list_or_404(Notebook)
        serializer = Notebooks(notebooks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Creates new notebook.
        ---
        parameters:
            - name: name
              description: Name for notebook.
              required: true
              type: string
              paramType: form

        responseMessages:
            - code: 201
              message: Created
            - code: 400
              message: Wrong entry
            - code: 401
              message: Not authenticated
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
        """Retrieve notebook with notebook_id.
        ---
        request_serializer: notes.apps.writer.resources.Notebooks

        responseMessages:
            - code: 200
              message: List of all notebooks
            - code: 404
              message: Not found
            - code: 401
              message: Not authenticated

        """
        notebook = get_object_or_404(Notebook, id=notebook_id, user=request.user)
        serializer = Notebooks(notebook)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, notebook_id):
        """Delete notebook with notebook_id.
        ---
        responseMessages:
            - code: 204
              message: Notebook is deleted
        """
        Notebook.objects.filter(id=notebook_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NoteList(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)

    def get(self, request, notebook_id):
        """List all notes from notebook with notebook_id.
        ---
        request_serializer: notes.apps.writer.resources.Notes

        responseMessages:
            - code: 200
              message: List of all notes in notebook.
            - code: 404
              message: No notes
        """
        notes = get_list_or_404(Note, notebook__id=notebook_id)
        serializer = Notes(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, notebook_id):
        """Create note in notebook with notebook_id.
        ---
        parameters:
            - name: title
              description: Title for note
              required: true
              type: string
              paramType: form
            - name: content
              description: content for note.
              required: false
              type: string
              paramType: form

        responseMessages:
            - code: 201
              message: Created
            - code: 400
              message: Must contain title
            - code: 404
              message: Notebook does not exist
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
        """Read note with note_id.
        ---
        request_serializer: notes.apps.writer.resources.Notes

        responseMessages:
            - code: 200
              message: Note found
            - code: 404
              message: Note or notebook does not exist

        """
        note = get_object_or_404(Note, id=note_id, notebook__id=notebook_id)
        serializer = Notes(note)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, notebook_id, note_id):
        """Update note.
        ---
        request_serializer: notes.apps.writer.resources.Notes

        responseMessages:
            - code: 204
              message: Note is updated
            - code: 400
              message: Must contain title
            - code: 404
              message: Note does not exist
        """
        note = get_object_or_404(Note, id=note_id, notebook__id=notebook_id)
        serializer = Notes(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, notebook_id, note_id):
        """Delete note.
        ---
        responseMessages:
            - code: 204
              message: Note is deleted
        """
        Note.objects.filter(id=note_id, notebook__id=notebook_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)









