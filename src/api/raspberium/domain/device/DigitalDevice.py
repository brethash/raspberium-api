from pyHS100 import SmartPlug

from src.api.raspberium import RaspberiumDevice


class DigitalDevice(RaspberiumDevice):
    def __init__(self, address):
        super().__init__()
        self.digitalOutputDevice = SmartPlug(address)

    def on(self):
        self.digitalOutputDevice.turn_on()
        self.digitalOutputDevice.led = True

    def off(self):
        self.digitalOutputDevice.turn_off()
        self.digitalOutputDevice.led = False
