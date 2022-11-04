from datetime import datetime
from unicodedata import name

from django.shortcuts import render
import requests

from dotenv import load_dotenv
import os

from . import models
from .models import City
from django.db import connection
from django.contrib.auth.decorators import login_required

 
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



@login_required

def api_favoris(request):
  
    sql="SELECT name FROM meteoapp_city GROUP BY name ORDER BY COUNT(*) DESC LIMIT 1 OFFSET 1"
    

       
    with connection.cursor() as cursor:
        cursor.execute(sql)
        villes=cursor.fetchall()   
        print(villes)     
        print(connection.queries)
    liste = []
  
    for ville in villes:
        ville = ville[0]
        
        request.session['city']=ville
        obj=models.City()
        obj.name=ville
        appid : SECRET_KEY 
        
        URL="https://api.openweathermap.org/data/2.5/weather"
        PARAMS= {'q':ville,'appid':SECRET_KEY ,'units':'metric'}
        

        city_weather = requests.get(url=URL ,params=PARAMS)
        
    
    

        res=city_weather.json()
        liste.append(res)
        
         
        description=liste[0]['weather'][0]['description']
        icon=liste[0]['weather'][0]['icon'] 
        temp=liste[0]['main']['temp'] 
        day = datetime.today()
    
    
        print(liste)    
        return render(request, 'favori.html',{'description':description,'icon':icon,'temp':temp, 'day':day,'name':villes})


        
