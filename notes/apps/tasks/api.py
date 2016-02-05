from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status, authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from notes.apps.account.models import User
from notes.apps.tasks.models import Task, Comment
from notes.apps.tasks.resources import Tasks, Comments, TaskStatus


class TaskList(APIView):
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (authentication.TokenAuthentication,)

    # shows all tasks (not necessary)
    # def get(self, request):
    #     """Retrieves all tasks admin has created.
    #     ---
    #     request_serializer: notes.apps.tasks.resources.Tasks

    #     responseMessages:
    #         - code: 200
    #           message: Retrieval succeeded.
    #         - code: 404
    #           message: No tasks found.
    #         - code: 401
    #           message: Unauthorized.
    #     """
    #     tasks = get_list_or_404(Task)
    #     serializer = Tasks(tasks, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Creates a new task.
        ---
        parameters:
            - name: asigned_to
              description: user id
              required: true
              type: integer
              paramType: form
            - name: name
              description: Task name.
              required: true
              type: string
              paramType: form
            - name: description
              description: what is expected of a task
              required: false
              type: string
              paramType: form
            - name: status
              description: (new=1, in_progress=2, done=3, closed=4)
              required: true
              type: choice
              paramType: form

        responseMessages:
            - code: 201
              message: Task created.
            - code: 400
              message: Invalid or missing data provided.
            - code: 401
              message: Unauthorized.
        """
        serializer = Tasks(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class UserTasks(APIView):

    def get(self, request, asigned_to):
        """Retrieves all tasks user has been assigned to.
        ---
        request_serializer: notes.apps.tasks.resources.Tasks

        responseMessages:
            - code: 200
              message: Retrieval succeeded.
            - code: 404
              message: No tasks found.
            - code: 401
              message: Unauthorized.
        """

        user = get_object_or_404(User, e_mail=asigned_to)
        tasks = get_list_or_404(Task, asigned_to=user.id)
        serializer = Tasks(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TaskDetail(APIView):

    def put(self, request, task_id):
        """Updates task status.
        ---
        request_serializer: notes.apps.tasks.resources.TaskStatus

        responseMessages:
            - code: 204
              message: Task status has been updated.
            - code: 400
              message: Invalid or missing data supplied.
            - code: 404
              message: Non-existent resource required.
        """
        task = get_object_or_404(Task, id=task_id)
        serializer = TaskStatus(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentList(APIView):

    def get(self, request, task_id):
        """Retrieves all comments from a specified task
        ---
        request_serializer: notes.apps.tasks.resources.Comments

        responseMessages:
            - code: 200
              message: Retrieval succeeded.
            - code: 404
              message: No comments.
        """

        comments = get_list_or_404(Comment, task__id=task_id)
        serializer = Comments(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, task_id):
        """Adds new comment to the specified task.
        ---
        parameters:
            - name: text
              description: comment text.
              required: true
              type: string
              paramType: form

        responseMessages:
            - code: 201
              message: Comment has been posted.
            - code: 400
              message: Invalid or missing data supplied.
            - code: 404
              message: Required task doesn't exist.
        """
        task = get_object_or_404(Task, id=task_id)
        serializer = Comments(data=request.data)
        if serializer.is_valid():
            serializer.save(task=task)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):

    def get(self, request, task_id, comment_id):
        """Retrieves content of a particular comment.
        ---
        request_serializer: notes.apps.tasks.resources.Comments

        responseMessages:
            - code: 200
              message: Retrieval succeeded.
            - code: 404
              message: Non-existent resource required.

        """
        note = get_object_or_404(Comment, id=comment_id, task__id=task_id)
        serializer = Comments(note)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, task_id, comment_id):
        """Updates a particular comment.
        ---
        request_serializer: notes.apps.tasks.resources.Comments

        responseMessages:
            - code: 204
              message: Comment has been updated.
            - code: 400
              message: Invalid or missing data supplied.
            - code: 404
              message: Non-existent resource required.
        """
        comment = get_object_or_404(Comment, id=comment_id, task__id=task_id)
        serializer = Comments(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, task_id, comment_id):
        """Removes selected comment.
        ---
        responseMessages:
            - code: 204
              message: Note has been removed.
        """
        Comment.objects.filter(id=comment_id, task__id=task_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
