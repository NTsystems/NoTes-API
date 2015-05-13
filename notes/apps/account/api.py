from django.contrib.auth import authenticate

from rest_framework import status, authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from notes.apps.account.resources import Account, Profile


class Register(APIView):
    """Create new User"""
    def post(self, request):
        """ Create user

        Args:
            request (str): The first parameter
        Returns:
            HTTP_400_BAD_REQUEST or
            HTTP_201_CREATED if user is created
        """
        serializer = Account(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TokenView(APIView):
    """Create tokens"""
    def post(self, request):
        """ Create token

        Args:
            request (str): The first parameter
        Returns:
            HTTP_400_BAD_REQUEST or
            HTTP_201_CREATED if token is created
        """
        e_mail = request.data.get('e_mail')
        password = request.data.get('password')
        user = authenticate(username=e_mail, password=password)

        if user is not None and user.is_active:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(token.key, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class UpdateProfile(APIView):
    """Update user profile"""

    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)

    def put(self, request, id):
        """ Create or update user profile

        Args:
            request (str): The first parameter
            id (int): The second parameter.User id.
        Returns:
            HTTP_400_BAD_REQUEST or
            HTTP_401_UNAUTHORIZED or
            HTTP_204_NO_CONTENT if user profile is update
        """
        serializer = Profile(request.user.profile, data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.validated_data, status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




























