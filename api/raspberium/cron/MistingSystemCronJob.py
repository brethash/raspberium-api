import time

from django_cron import CronJobBase, Schedule
import logging

from api.raspberium.domain.device.DigitalDevice import DigitalDevice
from api.raspberium.models import Device


class MistingSystemCronJob(CronJobBase):
    RUN_EVERY_MINS = 120

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'raspberium.misting_system'

    def do(self):
        log = logging.getLogger()
        try:
            misting_system = Device.objects.get(name__exact="misting-system")
        except Device.DoesNotExist:
            log.exception("Misting System not configured.")
        else:
            if misting_system.state == "auto":
                device = DigitalDevice(misting_system.address)
                device.on()
                time.sleep(8)
                device.off()
