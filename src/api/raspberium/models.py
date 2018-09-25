from django.db import models
from django.db.models import ManyToManyField
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
    pin = models.IntegerField(blank=True, default=0,
                              help_text="This is the physical pin that the device is connected to.")
    # state of the pin
    state = models.CharField(max_length=4, choices=State.choices, help_text="This is the default state of the device.")
    # status of the device
    status = models.CharField(max_length=3, editable=False, default=Status.Off)
    # the IP address of the Kasa Smart Plug
    address = models.CharField(max_length=15, default="000.000.000.000", blank=True,
                               help_text="This is the address of a Kasa Smart Plug.")

    def __str__(self):
        return "{} - {}".format(self.label, self.name, self.pin, self.state, self.status, self.address)

    class Meta:
        ordering = ('label',)
        verbose_name = 'device'
        verbose_name_plural = 'devices'

    @staticmethod
    def to_dict(instance):
        opts = instance._meta
        data = {}
        for f in opts.concrete_fields + opts.many_to_many:
            if isinstance(f, ManyToManyField):
                if instance.pk is None:
                    data[f.name] = []
                else:
                    data[f.name] = list(f.value_from_object(instance).values_list('pk', flat=True))
            else:
                data[f.name] = f.value_from_object(instance)
        return data
