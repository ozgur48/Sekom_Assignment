import requests

from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from .models import Weather, Provience, Town
from .serializers import WeatherSerializer, ProvienceSerializer, TownSerializer
import os

# Create your views here.
#restFramework CRUD standart
class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

class ProvienceViewSet(viewsets.ModelViewSet):
    queryset = Provience.objects.all()
    serializer_class = ProvienceSerializer

class TownViewSet(viewsets.ModelViewSet):
    queryset = Town.objects.all()
    serializer_class = TownSerializer

def provience(request):
    provience_list = Provience.objects.all()
    return render(request, 'weather/provience.html',  { 'provience_list':provience_list})

def result(request,provienceId):
    provience = Provience.objects.get(pk=provienceId)

    for town in provience.town_set.all():
        currentWeatherTown = getCurrentWeather(town.name + ", " + provience.name)
        if town.weather is not None:
            town.weather.delete()
        town.weather = currentWeatherTown
        town.save()
    
    currentWeather = getCurrentWeather(provience.name)
    oldProvienceWeather = provience.weather
    if oldProvienceWeather is not None:
        oldProvienceWeather.delete()
    
    provience.weather = currentWeather
    provience.save()
        
    return render(request, 'weather/result.html', { 'provience':provience })

def getCurrentWeather(location):
    url = os.environ.get("WEATHER_API_URL") + "?key=" + os.environ.get("WEATHER_API_KEY") + "&aqi=no&q=" + location
    response = requests.get(url) 
    jsonResponse = response.json()
    currentWeather = Weather( last_updated_epoch = jsonResponse['current']['last_updated_epoch'], temp_c = jsonResponse['current']['temp_c'], feelslike_c=jsonResponse['current']['feelslike_c'], 
        condition_text = jsonResponse['current']['condition']['text'], condition_icon = jsonResponse['current']['condition']['icon'], wind_kph = jsonResponse['current']['wind_kph'], 
        wind_dir = jsonResponse['current']['wind_dir'], humidity = jsonResponse['current']['humidity'] )
    currentWeather.save()
    
    return currentWeather

def index(request):
    return HttpResponse("Hello, world. You're at the weather index.")
