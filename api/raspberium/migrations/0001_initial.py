# Generated by Django 2.1.2 on 2018-11-17 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('pin', models.IntegerField(blank=True, default=0, help_text='This is the physical pin that the device is connected to.')),
                ('state', models.CharField(choices=[('off', 'Off'), ('on', 'On'), ('auto', 'Auto')], help_text='This is the default state of the device.', max_length=4)),
                ('status', models.CharField(default='off', editable=False, max_length=3)),
                ('address', models.CharField(blank=True, default='000.000.000.000', help_text='This is the address of a Kasa Smart Plug.', max_length=15)),
            ],
            options={
                'verbose_name': 'device',
                'verbose_name_plural': 'devices',
                'ordering': ('label',),
            },
        ),
    ]
