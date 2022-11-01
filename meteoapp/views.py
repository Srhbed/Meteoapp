from datetime import datetime
from unicodedata import name

from django.shortcuts import render
import requests

from dotenv import load_dotenv
import os
# from meteoapp.forms import Cityform 
# from django.forms import ModelForm , TextInput
from . import models
 
load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
def index(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city='Amsterdam'
    
    request.session['city']=city
    obj=models.City()
    obj.name=city
    obj.save()
    appid : SECRET_KEY 
    
    URL="https://api.openweathermap.org/data/2.5/weather"
    PARAMS= {'q':city,'appid':SECRET_KEY ,'units':'metric'}
    

    city_weather = requests.get(url=URL ,params=PARAMS)
  

    res=city_weather.json()
    description =res['weather'][0]['description']
    icon=res['weather'][0]['icon'] 
    temp =res['main']['temp'] 
    day = datetime.today()
   
    

   
    return render(request, 'home.html',{'description': description ,'icon':icon ,'temp':temp ,'day':day, 'city':city})

   
    
    
   

