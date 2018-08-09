from django.http import JsonResponse

from api.raspberium.domain.device.DigitalDevice import DigitalDevice
from api.raspberium.models import Device
from api.raspberium.serializers import DeviceSerializer


class DigitalDeviceProcessor:
    def __init__(self, device):
        self.device = (Device)(device)
        self.digitalDevice = DigitalDevice(device.pin)

    def on(self):
        try:
            self.digitalDevice.on()
            self.device.Status = self.device.Status.On
            serializer = DeviceSerializer(self.device)
            if serializer.is_valid():
                serializer.save()
        except:
            return "{0} could not be turned on.".format(self.device.label)

        return "%s was turned on." % self.device.label

    def off(self):
        try:
            self.digitalDevice.off()
            self.device.Status = self.device.Status.Off
            serializer = DeviceSerializer(self.device)
            if serializer.is_valid():
                serializer.save()
        except:
            return "%s could not be turned off." % self.device.label

        return "%s was turned off." % self.device.label
