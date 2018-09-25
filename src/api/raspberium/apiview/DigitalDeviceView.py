from django.http import Http404
from pyHS100 import Discover
from rest_framework.response import Response
from rest_framework.views import APIView

from src.api.raspberium import Device
from src.api.raspberium.processors import DigitalDeviceProcessor
from src.api.raspberium import SmartPlugSerializer


class DigitalDeviceApiView(APIView):

    def setup_device(self, device_name):
        try:
            return Device.objects.get(name__exact=device_name)
        except Device.DoesNotExist:
            raise Http404


class DigitalDeviceAddresses(APIView):

    def get(self, request, version, format=None):
        discoverResponse = Discover.discover()
        serlializer = SmartPlugSerializer()
        return Response(serlializer.discover_to_serializable(discoverResponse))


class DigitalDeviceOn(DigitalDeviceApiView):

    def get(self, request, version, device_name, format=None):
        device = self.setup_device(device_name)
        return DigitalDeviceProcessor(device).on()


class DigitalDeviceOff(DigitalDeviceApiView):

    def get(self, request, version, device_name, format=None):
        device = self.setup_device(device_name)
        return DigitalDeviceProcessor(device).off()
