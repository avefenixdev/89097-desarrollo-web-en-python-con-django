from django.shortcuts import render

def buscar(request):
    return render(request, "cursos/buscar.html")