from django.shortcuts import render
from .forms import CursoForm

def buscar(request):
    texto = request.GET.get("q", "")
    return render(request, "cursos/buscar.html", {"texto": texto})

def crear_curso(request):
    
    if request.method == "POST":
        formulario = CursoForm(request.POST) # no se asegura que los datos sean válidos
        if formulario.is_valid():
            datos = formulario.cleaned_data
            print(datos)
    else: # GET
        formulario = CursoForm()
    
    return render(request, "cursos/crear-curso.html", { "formulario": formulario})