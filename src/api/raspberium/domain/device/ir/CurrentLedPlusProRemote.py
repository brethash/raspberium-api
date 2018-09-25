from py_irsend import irsend

from src.api.raspberium.domain.device.ir.remotes import CurrentLedPlusPro


class CurrentLedPlusProRemote:
    def __init__(self):
        self.remote = "CurrentLedPlusPro"

    def sendCode(self, code):
        irsend.send_once(self.remote, [str(code)])

    def list_codes(self):
        return irsend.list_codes(self.remote)

    def on(self):
        self.sendCode(CurrentLedPlusPro.ON)

    def off(self):
        self.sendCode(CurrentLedPlusPro.OFF)

    def power(self):
        self.sendCode(CurrentLedPlusPro.POWER)

    def set_clock(self):
        self.sendCode(CurrentLedPlusPro.SET_CLOCK)

    def timer_on(self):
        self.sendCode(CurrentLedPlusPro.TIMER_ON)

    def timer_off(self):
        self.sendCode(CurrentLedPlusPro.TIMER_OFF)

    def plus_hour(self):
        self.sendCode(CurrentLedPlusPro.PLUS_HOUR)

    def minus_minute(self):
        self.sendCode(CurrentLedPlusPro.MINUS_MINUTE)

    def enter(self):
        self.sendCode(CurrentLedPlusPro.ENTER)

    def resume(self):
        self.sendCode(CurrentLedPlusPro.RESUME)

    def red(self):
        self.sendCode(CurrentLedPlusPro.RED)

    def yellow(self):
        self.sendCode(CurrentLedPlusPro.YELLOW)

    def blue(self):
        self.sendCode(CurrentLedPlusPro.BLUE)

    def purple(self):
        self.sendCode(CurrentLedPlusPro.PURPLE)

    def red_up(self):
        self.sendCode(CurrentLedPlusPro.RED_UP)

    def green_up(self):
        self.sendCode(CurrentLedPlusPro.GREEN_UP)

    def purple_up(self):
        self.sendCode(CurrentLedPlusPro.PURPLE_UP)

    def white(self):
        self.sendCode(CurrentLedPlusPro.WHITE)

    def m1(self):
        self.sendCode(CurrentLedPlusPro.M1)

    def m2(self):
        self.sendCode(CurrentLedPlusPro.M2)

    def daylight(self):
        self.sendCode(CurrentLedPlusPro.DAYLIGHT)

    def moonlight(self):
        self.sendCode(CurrentLedPlusPro.MOONLIGHT)

    def blue_moon(self):
        self.sendCode(CurrentLedPlusPro.BLUE_MOON)

    def black_moon(self):
        self.sendCode(CurrentLedPlusPro.BLACK_MOON)

    def partly_cloudy(self):
        self.sendCode(CurrentLedPlusPro.PARTLY_CLOUDY)

    def sunny(self):
        self.sendCode(CurrentLedPlusPro.SUNNY)

    def mostly_cloudy(self):
        self.sendCode(CurrentLedPlusPro.MOSTLY_CLOUDY)

    def storm1(self):
        self.sendCode(CurrentLedPlusPro.STORM1)

    def storm2(self):
        self.sendCode(CurrentLedPlusPro.STORM2)

    def rain(self):
        self.sendCode(CurrentLedPlusPro.RAIN)