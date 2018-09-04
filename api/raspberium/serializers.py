from django.contrib.auth.models import User, Group
from pyHS100 import SmartPlug
from rest_framework import serializers

from api.raspberium.models import Device


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ("label", "name", "pin", "state", "status")


class SmartPlugSerializer(serializers.HyperlinkedModelSerializer):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def discover_to_serializable(self, discover_dict: dict):
        plugs = []
        for address, plug in discover_dict.items():
            plug_dict = self.smart_plug_to_dict(plug)
            plugs.append(plug_dict)

        return plugs

    @staticmethod
    def smart_plug_to_dict(plug: SmartPlug):
        plug_dict = {"address": plug.host,
                     "alias": plug.alias,
                     "state": plug.state,
                     "led": plug.led}

        return plug_dict
