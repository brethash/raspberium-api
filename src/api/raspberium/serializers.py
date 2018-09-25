from django.contrib.auth.models import User, Group
from pyHS100 import SmartPlug
from rest_framework import serializers

from src.api.raspberium import Device


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    label = serializers.CharField(max_length=255)
    # device
    name = serializers.CharField(max_length=255)
    # pin's physical number (NOT GPIO!!!)
    pin = serializers.IntegerField()
    # state of the pin
    state = serializers.CharField(max_length=4)
    # status of the device
    status = serializers.CharField(max_length=3)
    # the IP address of the Kasa Smart Plug
    address = serializers.CharField(max_length=15)

    def __init__(self, *args, **kwargs):
        super(DeviceSerializer, self).__init__(*args, **kwargs)

    def create(self, validated_data):
        return Device.objects.create(**validated_data)

    class Meta:
        model = Device
        fields = ("label", "name", "pin", "state", "status", "address")


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
