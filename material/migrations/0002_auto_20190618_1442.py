# Generated by Django 2.2.2 on 2019-06-18 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meterials',
            name='capacityRange',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='meterials',
            name='comFactor',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='meterials',
            name='velocityPressure',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]