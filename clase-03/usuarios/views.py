from django.shortcuts import render

def crear_usuario(request):
    return render(request, "usuarios/crear_usuario.html")