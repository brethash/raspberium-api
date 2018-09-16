# Generated by Django 2.1.1 on 2018-09-13 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raspberium', '0003_auto_20180904_0109'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='device',
            options={'ordering': ('label',), 'verbose_name': 'device', 'verbose_name_plural': 'devices'},
        ),
        migrations.AlterField(
            model_name='device',
            name='address',
            field=models.CharField(blank=True, default='000.000.000.000', help_text='This is the address of a Kasa Smart Plug.', max_length=15),
        ),
        migrations.AlterField(
            model_name='device',
            name='pin',
            field=models.IntegerField(blank=True, default=0, help_text='This is the physical pin that the device is connected to.'),
        ),
    ]
