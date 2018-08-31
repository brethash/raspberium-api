from rest_framework.response import Response
from rest_framework.views import APIView

from api.raspberium.domain.device.ir.CurrentLedPlusProRemote import CurrentLedPlusProRemote


class CurrentLedPlusProView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.remote = CurrentLedPlusProRemote()


class CurrentLedPlusProOn(CurrentLedPlusProView):

    def get(self, request, version, format=None):
        action = CurrentLedPlusProRemote.on(self.remote)
        return Response({action})


class CurrentLedPlusProOff(CurrentLedPlusProView):

    def get(self, request, version, format=None):
        action = CurrentLedPlusProRemote.off(self.remote)
        return Response({action})


class CurrentLedPlusProPower(CurrentLedPlusProView):

    def get(self, request, version, format=None):
        action = CurrentLedPlusProRemote.power(self.remote)
        return Response({action})
