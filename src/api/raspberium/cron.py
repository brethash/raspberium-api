from src.api.raspberium import Bme280


def checkHumidity():
    """TODO: need to define configurations and thresholds"""
    humidity = Bme280.getHumidity()

