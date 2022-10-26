from datetime import datetime
from django.shortcuts import render
import requests
from django.http import HttpResponse  


def index(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city='Amsterdam'
    
    request.session['city']=city
    
    appid= '12e30bac05ff8b5c1f2adf2be1c7be2b'
    
    URL="https://api.openweathermap.org/data/2.5/weather"
    PARAMS= {'q':city,'appid':appid ,'units':'metric'}
    

    city_weather = requests.get(url=URL ,params=PARAMS)

    res=city_weather.json()
    description =res['weather'][0]['description']
    icon=res['weather'][0]['icon'] 
    temp =res['main']['temp'] 
    day = datetime.today()
    

   
    return render(request, 'home.html',{'description': description ,'icon':icon ,'temp':temp ,'day':day, 'city':city})

 
   

