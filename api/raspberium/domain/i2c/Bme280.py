import smbus2
import bme280


class Bme280():
    def __init__(self):
        """ need to implement caching for temp, water, and pressure to avoid data collisions"""
        self.port = 1
        self.address = 0x76
        self.bus = smbus2.SMBus(self.port)

    def debug(self):
        bme280.load_calibration_params(self.bus, self.address)

        # the sample method will take a single reading and return a
        # compensated_reading object
        data = bme280.sample(self.bus, self.address)

        print("compensation_params = {0}".format(bme280.compensation_params))

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
        bme280.load_calibration_params(self.bus, self.address)
        data = bme280.sample(self.bus, self.address)

        return data.temperature

    def getHumidity(self):
        bme280.load_calibration_params(self.bus, self.address)

        data = bme280.sample(self.bus, self.address)

        return data.humidity

    def getPressure(self):
        bme280.load_calibration_params(self.bus, self.address)

        data = bme280.sample(self.bus, self.address)

        return data.pressure
