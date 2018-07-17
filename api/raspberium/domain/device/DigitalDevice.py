from gpiozero import DigitalOutputDevice

from api.raspberium.domain.device.RaspberiumDevice import RaspberiumDevice


class DigitalDevice(RaspberiumDevice):
    def __init__(self, pin):
        super().__init__()
        self.digitalOutputDevice = DigitalOutputDevice(pin)

    def on(self):
        self.digitalOutputDevice.on()

    def off(self):
        self.digitalOutputDevice.off()