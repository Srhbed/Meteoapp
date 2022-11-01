from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import *
from datetime import datetime
import requests




def index(request):
    return render(request , 'A_Propos.html')

class SignUp(CreateView):
    form_class= UserCreationForm
    success_url= reverse_lazy('login')
    template_name= 'registration/signup.html'
   





def favori(request):
    if 'city' in request.POST:
        city = request.POST['city']

    
  
    appid= '12e30bac05ff8b5c1f2adf2be1c7be2b'
    
    URL="https://api.openweathermap.org/data/2.5/weather"
    PARAMS= {'q':city,'appid':appid ,'units':'metric'}
    

    city_weather = requests.get(url=URL ,params=PARAMS)
  

    res=city_weather.json()
    description =res['weather'][0]['description']
    icon=res['weather'][0]['icon'] 
    temp =res['main']['temp'] 
    day = datetime.today()
   
    

   
    return render(request, 'favori.html',{'description': description ,'icon':icon ,'temp':temp ,'day':day, 'city':city})

   
    
    
   







