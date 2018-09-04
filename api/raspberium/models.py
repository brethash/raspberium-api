from django.db import models
from djchoices import ChoiceItem
from djchoices import DjangoChoices


class Device(models.Model):
    class State(DjangoChoices):
        Off = ChoiceItem("off")
        On = ChoiceItem("on")
        Auto = ChoiceItem("auto")

    class Status(DjangoChoices):
        Off = ChoiceItem("off")
        On = ChoiceItem("on")

    # device display name
    label = models.CharField(max_length=255, null=False)
    # device
    name = models.CharField(max_length=255, null=False, unique=True)
    # pin's physical number (NOT GPIO!!!)
    pin = models.IntegerField(null=True, help_text="This is the physical pin that the device is connected to.")
    # state of the pin
    state = models.CharField(max_length=4, choices=State.choices, help_text="This is the default state of the device.")
    # status of the device
    status = models.CharField(max_length=3, editable=False, default=Status.Off)
    # the IP address of the Kasa Smart Plug
    address = models.CharField(max_length=15, null=True, help_text="This is the address of a Kasa Smart Plug.")

    def __str__(self):
        return "{} - {}".format(self.label, self.name, self.pin, self.state, self.status)

    class Meta:
        ordering = ('name',)
        verbose_name = 'device'
        verbose_name_plural = 'devices'
