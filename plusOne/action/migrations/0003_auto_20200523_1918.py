# Generated by Django 3.0.6 on 2020-05-23 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('action', '0002_auto_20200523_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='owner',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]