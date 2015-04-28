from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from notes.apps.account.models import User, UserProfile
from notes.apps.account.resources import UserSerializer, ProfileSerializer
from rest_framework import permissions


class CreateUser(APIView):
    """Create new User."""

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateProfile(APIView):
    """Update user profile"""
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request, id):
        try:
            profile = UserProfile.objects.get(id)

        except User.DoesNotExist:
            return Response(status=status.HTTP_403_FORBIDDEN)

        if permissions.IsAuthenticated:
            serializer = ProfileSerializer(profile, data=request.data['id'])

            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_401_UNAUTHORIZED)






















