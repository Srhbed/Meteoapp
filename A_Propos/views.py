from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    context = {"message" : "Hello World !"}
    template = loader.get_template("A_Propos/A_Propos.html")
    return HttpResponse(template.render(context, request))





# Create your views here.
