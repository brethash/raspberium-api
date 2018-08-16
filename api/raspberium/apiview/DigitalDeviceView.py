from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from api.raspberium.models import Device
from api.raspberium.processors.device.DigitalDeviceProcessor import DigitalDeviceProcessor


class DigitalDeviceApiView(APIView):

    def setup_device(self, device_name):
        try:
            return Device.objects.get(name__exact=device_name)
        except Device.DoesNotExist:
            raise Http404


class DigitalDeviceOn(DigitalDeviceApiView):

    def get(self, request, version, device_name, format=None):
        device = self.setup_device(device_name)
        action = DigitalDeviceProcessor(device).on()
        return Response({action})


class DigitalDeviceOff(DigitalDeviceApiView):

    def get(self, request, version, device_name, format=None):
        device = self.setup_device(device_name)
        action = DigitalDeviceProcessor(device).off()
        return Response({action})