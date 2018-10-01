from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is a bad request, use one of the other routes.")
# Create your views here.
def language (request):
    return HttpResponse("My fave language is PYTHON")
def system (request):
    return HttpResponse("Window is my fav OS tbh")
def IDE (request):
    return HttpResponse("IntelliJ only one I know so it wins")