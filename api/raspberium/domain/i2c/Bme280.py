import bme280
import smbus2
from cachetools import cached, TTLCache


class Bme280():
    # The BME280 has an average response time of 1s, so we'll try 2s to give it a little buffer.
    cache = TTLCache(maxsize=100, ttl=2000)

    def __init__(self):
        self.port = 1
        self.address = 0x76
        self.bus = smbus2.SMBus(self.port)

    @cached(cache)
    def debug(self):
        compensation_params = bme280.load_calibration_params(self.bus, self.address)

        data = self._getSensorData()

        print("compensation_params = {0}".format(compensation_params))

        # the compensated_reading class has the following attributes:
        #
        #   data.id
        #   data.timestamp
        #   data.temperature
        #   data.pressure
        #   data.water
        #   data.uncompensated

        print(data.uncompensated)

        # there is a handy string representation too
        print(data)

    def getTemperature(self):
        data = self._getSensorData()

        return data.temperature

    def getHumidity(self):
        data = self._getSensorData()

        return data.humidity

    def getPressure(self):
        data = self._getSensorData()

        return data.pressure

    @cached(cache)
    def _getSensorData(self):
        bme280.load_calibration_params(self.bus, self.address)
        return bme280.sample(self.bus, self.address)
