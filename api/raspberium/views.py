from django.contrib.auth.models import User, Group
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from api.raspberium.models import Device
from api.raspberium.processors.device.DigitalDeviceProcessor import DigitalDeviceProcessor
from api.raspberium.serializers import UserSerializer, GroupSerializer, DeviceSerializer


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


@api_view(['GET'])
def digital_device_on(request, version, device_name):
    device = setup_device(device_name)
    return DigitalDeviceProcessor(device).on()


def setup_device(device_name):

    device = Device.objects.get(name__exact=device_name)
    if not device:
        raise Http404

    return device
