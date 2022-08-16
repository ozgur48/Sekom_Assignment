from .models import Town, Provience, Weather
from rest_framework import serializers

class WeatherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'

class ProvienceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provience
        fields = ('provienceId', 'name', 'weather')

class TownSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Town
        fields = '__all__'

