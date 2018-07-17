from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from rest_framework import routers

from api.raspberium import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'devices', views.DevicesViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    re_path('api/(?P<version>(v1|v2))/', include('api.raspberium.urls'))
]