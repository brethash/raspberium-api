from api.raspberium.domain.i2c.Bme280 import Bme280
from api.raspberium.models import Device


def checkHumidity():
    """TODO: need to define configurations and thresholds"""
    humidity = Bme280.getHumidity()

