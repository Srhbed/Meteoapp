
from unicodedata import name
from django.forms import ModelForm , TextInput

from . import models
from .models import City



class Cityform(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            "name": TextInput({'class' : 'input', 'placeholder' : 'City Name'})

        }

   
            

   