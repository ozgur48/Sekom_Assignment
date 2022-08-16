from django.db import models

# Create your models here.

class Weather(models.Model):
    last_updated_epoch = models.IntegerField()
    temp_c = models.DecimalField(max_digits=3, decimal_places=1)
    feelslike_c = models.DecimalField(max_digits=3, decimal_places=1)
    condition_text = models.CharField( max_length = 1000 )
    condition_icon = models.CharField( max_length = 1000 )
    wind_kph = models.DecimalField(max_digits=4, decimal_places=1)
    wind_dir = models.CharField( max_length = 100 )
    humidity = models.IntegerField()

class Provience(models.Model):
    name = models.CharField( max_length=100, null=False )
    provienceId = models.IntegerField( primary_key=True )
    weather = models.OneToOneField( Weather, on_delete=models.SET_NULL, primary_key=False, null=True)
    def __str__(self):
        return self.name

class Town(models.Model):
    provience = models.ForeignKey( Provience, on_delete=models.CASCADE)
    name = models.CharField( max_length=100, null=False )
    weather = models.OneToOneField( Weather, on_delete=models.SET_NULL, primary_key=False, null=True)
    def __str__(self):
        return self.name
