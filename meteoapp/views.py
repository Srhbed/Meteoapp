from multiprocessing import context
from django.shortcuts import render
import requests
from . import forms
from requests import Session
from .models import City
from .forms import Cityform
import json


def index(request):
    
    cities = City.objects.all()
    key = '12e30bac05ff8b5c1f2adf2be1c7be2b'
    
    url="https://samples.openweathermap.org/data/2.5/weather?q={}&appid=b1b15e88fa797225412429c1c50c122a1"

    
    


    if request.method =="POST" :
        form = Cityform(request.POST)
        form.save()
    form = Cityform()
    weather_data = []    
    
    for city in cities :
        city_weather = requests.get(url.format(city)).json()
        
        
        weather = {
        'city' :city,
        'temperature' : city_weather['main']['temp'] ,
        'description ': city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon'] ,
        'humidity': city_weather ['main']['humidity'],
        'pressure' : city_weather['main']['pressure'],
        'windspeed' : city_weather['wind']['speed'],
        }
        
        weather_data.append(weather)
    context = {'weather_data' : weather_data , 'form': form}
    return render(request, 'index.html', context)
        

   
