# Generated by Django 4.1 on 2022-08-11 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_alter_provience_weather_alter_town_weather'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='feelslike_c',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='weather',
            name='temp_c',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='weather',
            name='wind_kph',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
    ]