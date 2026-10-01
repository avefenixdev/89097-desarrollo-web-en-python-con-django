from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# El archivo views de las aplicaciones son función (methods) que devuelve una respuesta o llaman a una plantilla

def inicio(request):
    return HttpResponse("Bienvenidos a Tiendita")
    