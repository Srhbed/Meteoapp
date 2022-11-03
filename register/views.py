from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import *
from datetime import datetime
import requests
from . import forms



def index(request):
    return render(request , 'A_Propos.html')

class SignUp(CreateView):
    form_class= forms.UserCreationFormCustom
    success_url= reverse_lazy('login')
    template_name= 'registration/signup.html'
   


   





   
    
    
   







