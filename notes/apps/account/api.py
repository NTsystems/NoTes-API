from django.contrib.auth import authenticate

from rest_framework import status, authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from notes.apps.account.resources import Account, Profile
from notes.apps.account.models import UserProfile

from notes.apps.account.tasks import activation_email_template


class Register(APIView):
    def post(self, request):
        """Creates new user account.
        ---
        parameters:
            - name: e_mail
              description: User's email address.
              required: true
              type: string
              paramType: form
            - name: password
              description: User's password.
              required: true
              type: string
              paramType: form

        responseMessages:
            - code: 201
              message: Registration succeeded.
            - code: 400
              message: Invalid or missing data supplied.
        """
        serializer = Account(data=request.data)
        

        if serializer.is_valid():
            serializer.save()
            try:
              activation_email_template.delay(serializer.data['id'])
            except Exception as e:
              print repr(e)
              
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TokenView(APIView):
    def post(self, request):
        """Creates or retrieves authentication token.
        ---
        parameters:
            - name: e_mail
              description: User's email address.
              required: true
              type: string
              paramType: form
            - name: password
              description: User's password.
              required: true
              type: string
              paramType: form

        responseMessages:
            - code: 201
            - code: 400
              message: Account inactive or non-existent.
        """
        e_mail = request.data.get('e_mail')
        password = request.data.get('password')
        user = authenticate(username=e_mail, password=password)

        if user is not None and user.is_active:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(token.key, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class UpdateProfile(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)

    def put(self, request, id):
        """Updates user profile information.
        ---
        request_serializer: notes.apps.account.resources.Profile

        responseMessages:
            - code: 204
            - code: 400
              message: Invalid or missing data supplied.
            - code: 401
              message: Unauthorized.
        """
        serializer = Profile(data=request.data, context={'request': request})
        if serializer.is_valid():
            profile, _ = UserProfile.objects.update_or_create(user=request.user, defaults=request.data)
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)