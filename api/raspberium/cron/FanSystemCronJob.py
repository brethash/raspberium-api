import logging

from django_cron import CronJobBase, Schedule

from api.raspberium.domain.device.DigitalDevice import DigitalDevice
from api.raspberium.domain.i2c.Bme280 import Bme280
from api.raspberium.models import Device


class FanSystemCronJob(CronJobBase):
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'raspberium.fan_system'

    def do(self):
        log = logging.getLogger()
        try:
            fan_system = Device.objects.get(name__exact="fan-system")
        except Device.DoesNotExist:
            log.exception("Fan System not configured.")
        else:
            if fan_system.state == "auto":
                humidity = Bme280().getHumidity()
                device = DigitalDevice(fan_system.address)
                if humidity < 80:
                    device.off()
                elif humidity > 90:
                    device.on()
