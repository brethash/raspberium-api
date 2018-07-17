from py_irsend import irsend

from api.raspberium.domain.device.ir.remotes.CurrentLedPlusPro import CurrentLedPlusPro
from api.raspberium.models import Device


class IrRemote(Device):
    def __init__(self):
        super().__init__()
        self.remote = "CurrentLedPlusPro"

    def sendCode(self, code):
        irsend.send_once(self.remote, code)

    def on(self):
        self.sendCode(CurrentLedPlusPro.ON)

    def off(self):
        self.sendCode(CurrentLedPlusPro.OFF)
