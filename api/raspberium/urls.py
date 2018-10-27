from django.conf.urls import url
from django.urls import include

from api import urls
from api.raspberium.apiview import DigitalDeviceView, SystemStatus
from api.raspberium.apiview.CurrentLedPlusProView import *

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
    url(r'^system/status/temperature', SystemStatus.SystemStatusTemperature.as_view(), name='urlname'),
    url(r'^system/status/humidity', SystemStatus.SystemStatusHumidity.as_view(), name='urlname'),
    url(r'^system/status/pressure', SystemStatus.SystemStatusPressure.as_view(), name='urlname'),
    url(r'^system/status/debug', SystemStatus.SystemStatusDebug.as_view(), name='urlname'),
]
