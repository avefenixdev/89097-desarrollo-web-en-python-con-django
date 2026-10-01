from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    # return HttpResponse("Hola desde Django")
    return render(request, "catalogo/inicio.html")
