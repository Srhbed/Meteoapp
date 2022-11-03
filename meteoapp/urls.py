from django.urls import path
from . import views



urlpatterns = [
    path('',views.index,name='home'),
    path('favori/',views.api_favoris, name='favori'),

    
]