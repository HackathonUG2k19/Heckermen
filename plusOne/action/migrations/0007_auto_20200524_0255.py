# Generated by Django 3.0.6 on 2020-05-23 21:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('action', '0006_auto_20200524_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='journey_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 23, 21, 25, 10, 255799, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='trip',
            name='journey_time',
            field=models.TimeField(default=datetime.datetime(2020, 5, 23, 21, 25, 10, 293254, tzinfo=utc)),
        ),
    ]
