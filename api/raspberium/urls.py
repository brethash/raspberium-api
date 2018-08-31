from django.conf.urls import url
from django.urls import include

from api import urls
from api.raspberium.apiview import DigitalDeviceView
from api.raspberium.apiview.CurrentLedPlusProView import *

app_name = "raspberium"

router = urls.router

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^device/(?P<device_name>[a-z0-9]+)/on$', DigitalDeviceView.DigitalDeviceOn.as_view(), name='urlname'),
    url(r'^device/(?P<device_name>[a-z0-9]+)/off$', DigitalDeviceView.DigitalDeviceOff.as_view(), name='urlname'),
    url(r'^device/ir-remote/on', CurrentLedPlusProOn.as_view(), name='urlname'),
    url(r'^device/ir-remote/off', CurrentLedPlusProOff.as_view(), name='urlname'),
    url(r'^device/ir-remote/power', CurrentLedPlusProPower.as_view(), name='urlname'),
]
