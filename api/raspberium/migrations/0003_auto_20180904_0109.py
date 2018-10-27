# Generated by Django 2.0.6 on 2018-09-04 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raspberium', '0002_auto_20180901_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='pin',
            field=models.IntegerField(help_text='This is the physical pin that the device is connected to.', null=True),
        ),
    ]