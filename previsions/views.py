from datetime import datetime
from django.shortcuts import render
import requests

from meteoapp.views import SECRET_KEY







def previsions(request):
    
    
    city =request.session['city']

    URL="http://api.openweathermap.org/data/2.5/forecast?"
    api_key : SECRET_KEY
 
    NEWPARAMS ={'appid': SECRET_KEY , 'q':city , 'units':'metric'}

    
    previsions_meteo=requests.get(url=URL,params=NEWPARAMS)
    response=previsions_meteo.json()
    print(response)

    temp0=response["list"][0]["main"]["temp"]
    ressentie0=response["list"][0]["main"]["feels_like"]
    dt0=response["list"][0]["dt_txt"]
    icon0=response['list'][0]['weather'][0]['icon'] 
    wind0=response["list"][0]["wind"]["speed"]
    description0=response["list"][0]["weather"][0]["description"]
    
    temp10=response["list"][10]["main"]["temp"]
    ressentie10=response["list"][10]["main"]["feels_like"]
    dt10=response["list"][10]["dt_txt"]
    icon10=response['list'][10]['weather'][0]['icon'] 

    wind10=response["list"][10]["wind"]["speed"]
    description10=response["list"][10]["weather"][0]["description"]


    temp15=response["list"][15]["main"]["temp"]
    ressentie15=response["list"][15]["main"]["feels_like"]
    dt15=response["list"][15]["dt_txt"]
    icon15=response['list'][15]['weather'][0]['icon'] 

    wind15=response["list"][15]["wind"]["speed"]
    description15=response["list"][15]["weather"][0]["description"]


    temp20=response["list"][20]["main"]["temp"]
    ressentie20=response["list"][20]["main"]["feels_like"]
    dt20=response["list"][20]["dt_txt"]
    icon20=response['list'][20]['weather'][0]['icon'] 
    wind20=response["list"][20]["wind"]["speed"]
    description20=response["list"][20]["weather"][0]["description"]


    temp30=response["list"][30]["main"]["temp"]
    ressentie30=response["list"][30]["main"]["feels_like"]
    dt30=response["list"][30]["dt_txt"]
    icon30=response['list'][30]['weather'][0]['icon'] 
    wind30=response["list"][30]["wind"]["speed"]
    description30=response["list"][30]["weather"][0]["description"]


    temp39=response["list"][39]["main"]["temp"]
    ressentie39=response["list"][39]["main"]["feels_like"]
    dt39=response["list"][39]["dt_txt"]
    icon39=response['list'][39]['weather'][0]['icon'] 
    wind39=response["list"][39]["wind"]["speed"]
    description39=response["list"][39]["weather"][0]["description"]
    
    return render(request, 'previsions.html',{ 'temp0':temp0 ,'ressenti0':ressentie0,'dt0':dt0 ,'icon0':icon0,'wind0':wind0,'description0': description0 ,'temp10':temp10 ,'ressenti10':ressentie10,'dt10':dt10 ,"icon10":icon10,'wind10':wind10,'description10': description10 ,'temp15':temp15 ,'ressenti15':ressentie15,'dt15':dt15 ,'icon15':icon15,'wind15':wind15,'description15': description15, 'temp20':temp20 ,'ressenti20':ressentie20,'dt20':dt20 ,'icon20':icon20,'wind20':wind20,'description20': description20 ,'temp30':temp30 ,'ressenti30':ressentie30,'dt30':dt30 ,'icon30':icon30,'wind30':wind30,'description30': description30 ,'temp39':temp39 ,'ressenti39':ressentie39,'dt39':dt39 ,'icon39':icon39,'wind39':wind39,'description39': description39 ,'city':city })


