from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from api.raspberium.domain.device.DigitalDevice import DigitalDevice
from api.raspberium.models import Device
from api.raspberium.serializers import DeviceSerializer


class DigitalDeviceProcessor:
    def __init__(self, device: Device):
        self.device = device
        self.digitalDevice = DigitalDevice(device.address)

    def on(self):
        self.digitalDevice.on()
        self.device.status = self.device.Status.On
        return self.flip_the_switch()

    def off(self):
        self.digitalDevice.off()
        self.device.status = self.device.Status.Off
        return self.flip_the_switch()

    def flip_the_switch(self):
        device_data = self.device.to_dict(self.device)
        serializer = DeviceSerializer(self.device, data=device_data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except ValidationError:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.data, status=status.HTTP_200_OK)
