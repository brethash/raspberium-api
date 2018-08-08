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
            error_string = "{0} could not be turned on.".format(self.device.label)
            return JsonResponse([error_string], safe=False)

        return JsonResponse(["%s was turned on." % self.device.label], safe=False)

    def off(self):
        try:
            self.digitalDevice.off()
            self.device.Status = self.device.Status.Off
            serializer = DeviceSerializer(self.device)
            if serializer.is_valid():
                serializer.save()
        except:
            return JsonResponse(["%s could not be turned off." % self.device.label], safe=False)

        return JsonResponse(["%s was turned off." % self.device.label], safe=False)
