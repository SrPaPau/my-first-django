from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hello(request):
    return HttpResponse("<h1>Hola mundo</h1>")


def about(request):
    return HttpResponse("<h1>about</h1>")


def SaludoPersonal(request, username):
    return HttpResponse("<h1>Hello %s</h1>" % username)

def idProyecto(request, idProyecto):
    return HttpResponse("<h1>Hello %s</h1>" % idProyecto)