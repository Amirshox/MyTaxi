from django.shortcuts import render
from rest_framework import viewsets

from users.models import User
from users.serializers import UserCreateSerializer, UserModelSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return super().get_serializer_class()
