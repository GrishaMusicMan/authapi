from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializer import RegisterSerializer, UpdateUserSerializer

User = get_user_model()


class RegisterUserAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny, )


class UpdateUserNameView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
    permission_classes = (IsAuthenticated, )




