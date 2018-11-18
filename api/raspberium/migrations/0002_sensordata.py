# Generated by Django 2.1.2 on 2018-11-18 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raspberium', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('humidity', models.FloatField(editable=False)),
                ('temperature', models.FloatField(editable=False)),
                ('pressure', models.FloatField(editable=False)),
            ],
            options={
                'verbose_name': 'sensor_data',
                'verbose_name_plural': 'sensor_datum',
                'ordering': ('timestamp',),
            },
        ),
    ]
