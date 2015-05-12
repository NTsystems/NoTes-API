from django.contrib.auth import authenticate
from rest_framework import status, authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from notes.apps.account.resources import Account, Profile


class Register(APIView):
    """Create new User."""
    serializer_class = Account

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TokenView(APIView):
    """Create tokens."""
    def post(self, request):
        Account(data=request.data)
        e_mail = request.data.get('e_mail')
        password = request.data.get('password')
        user = authenticate(username=e_mail, password=password)

        if user is not None and user.is_active:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(token.key, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)



class UpdateProfile(APIView):
    """Update user profile"""
    serializer_class = Profile

    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)

    def put(self, request):
        if request.user.is_authenticated():
            profile = None
            if hasattr(request.user, 'userprofile'):
                profile = request.user.userprofile
            serializer = self.serializer_class(profile, data=request.data, context={'request': request})

            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.validated_data, status=status.HTTP_204_NO_CONTENT)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_401_UNAUTHORIZED)




























