from django.shortcuts import render
from .forms import UsuarioForm

def crear_usuario(request):
    
    if request.method == "POST":
        print('Hacemos algo')
    else: 
        form = UsuarioForm()
    
    return render(request, "usuarios/crear_usuario.html", {"form": form})