from django.conf.urls import url
from django.urls import include

from src.api import urls
from src.api.raspberium.apiview import DigitalDeviceView

app_name = "raspberium"

router = urls.router

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^device/available-addresses', DigitalDeviceView.DigitalDeviceAddresses.as_view(), name='urlname'),
    url(r'^device/(?P<device_name>[a-z-0-9]+)/on$', DigitalDeviceView.DigitalDeviceOn.as_view(), name='urlname'),
    url(r'^device/(?P<device_name>[a-z-0-9]+)/off$', DigitalDeviceView.DigitalDeviceOff.as_view(), name='urlname'),
    url(r'^device/ir-remote/on', CurrentLedPlusProOn.as_view(), name='urlname'),
    url(r'^device/ir-remote/off', CurrentLedPlusProOff.as_view(), name='urlname'),
    url(r'^device/ir-remote/power', CurrentLedPlusProPower.as_view(), name='urlname'),
]
