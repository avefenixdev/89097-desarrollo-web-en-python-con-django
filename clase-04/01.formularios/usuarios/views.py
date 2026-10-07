from django.shortcuts import render
from .forms import UsuarioForm

def crear_usuario(request):
    
    if request.method == "POST":
        print('Hacemos algo')
        form = UsuarioForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            # Se muestran tipos, sin imprimir datos personales
            print("Tipo de edad:", type(datos["edad"]).__name__)
            print("Tipo de nombre:", type(datos["nombre"].__name__))
        
        
    else: # GET -> Mostrar el formulario
        form = UsuarioForm()
    
    return render(request, "usuarios/crear_usuario.html", {"form": form})

def confirmacion(request): # http://localhost:8000/usuarios/confirmacion/confirmacion.html
    return render(request, "usuarios/confirmacion.html")