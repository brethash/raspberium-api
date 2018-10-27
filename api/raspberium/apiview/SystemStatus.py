from rest_framework.response import Response
from rest_framework.views import APIView

from api.raspberium.domain.i2c.Bme280 import Bme280


class SystemStatusView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sensor = Bme280()


class SystemStatusTemperature(SystemStatusView):

    def get(self, request, version, format=None):
        return Response({self.sensor.getTemperature()})


class SystemStatusHumidity(SystemStatusView):

    def get(self, request, version, format=None):
        return Response({self.sensor.getHumidity()})


class SystemStatusPressure(SystemStatusView):

    def get(self, request, version, format=None):
        return Response({self.sensor.getPressure()})


class SystemStatusDebug(SystemStatusView):

    def get(self, request, version, format=None):
        return Response({self.sensor.debug()})
