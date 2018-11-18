import logging

from django_cron import CronJobBase, Schedule

from api.raspberium.domain.i2c.Bme280 import Bme280
from api.raspberium.models import SensorData


class MonitoringCronJob(CronJobBase):
    RUN_EVERY_MINS = 10

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'raspberium.monitoring'

    def do(self):
        log = logging.getLogger()
        bme280 = Bme280()
        if bme280.bus is None:
            log.exception("BME280 not configured.")
        else:
            humidity = bme280.getHumidity()
            temperature = bme280.getTemperature()
            pressure = bme280.getPressure()
            sensor_data = SensorData(humidity=humidity, temperature=temperature, pressure=pressure)
            sensor_data.save()
