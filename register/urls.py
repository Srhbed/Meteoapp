from django.urls import path
from . import views
from   .views   import  SignUp






urlpatterns   =   [ 
     path  ( "", views.SignUp.as_view()), 
 ] 