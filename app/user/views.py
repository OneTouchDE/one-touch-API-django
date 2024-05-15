from django.shortcuts import render

from rest_framework import generics, authentication, permissions, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


from rest_framework.settings import api_settings
from user.serializers import (UserSerializer, AuthTokenSerializer)

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer

class CustomAuthToken(ObtainAuthToken):
    def post(self, request):
        serializer = self.serializer_class(data= request.data, context =  {'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        if created:
            return Response({
                'token': token.key,
                'name': user.name,
                'email': user.email,
            })
        else:
            return Response({
                'token': token.key,
                'name': user.name,
                'email': user.email,
            })

class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class LogoutView(generics.GenericAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        token = Token.objects.get(user=request.user)

        token.delete()
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)