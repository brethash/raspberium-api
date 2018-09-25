from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from .models import Device
from .serializers import DeviceSerializer


# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_device(name="", pin=0, state=Device.State.Off, status=Device.Status.Off):
        if name != "" and isinstance(pin, int) and isinstance(state, Device.State) and isinstance(status,
                                                                                                  Device.Status):
            Device.objects.create(name=name, pin=pin, state=state, status=status)

    def setUp(self):
        # add test data
        self.create_device("device 1", 1)
        self.create_device("device 2", 2)
        self.create_device("device 3", 3)
        self.create_device("device 4", 4)


class GetAllDevicesTest(BaseViewTest):
    def test_get_all_devices(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("device-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Device.objects.all()
        serialized = DeviceSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
