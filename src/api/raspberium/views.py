from django.contrib.auth.models import User, Group
from rest_framework import generics
from rest_framework import viewsets

from src.api.raspberium import Device
from src.api.raspberium import UserSerializer, GroupSerializer, DeviceSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class DevicesViewSet(generics.ListAPIView, viewsets.ModelViewSet):
    """
    Provides a get method handler.
    """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
