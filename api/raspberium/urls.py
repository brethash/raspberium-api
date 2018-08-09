from django.conf.urls import url
from django.urls import include

from api import urls
from api.raspberium import views

app_name = "raspberium"

router = urls.router

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^device/(?P<device_name>[a-z0-9]+)/on$', views.digital_device_on, name='urlname'),
]
