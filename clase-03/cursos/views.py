from django.shortcuts import render
from .forms import CursoForm

def buscar(request):
    texto = request.GET.get("q", "")
    return render(request, "cursos/buscar.html", {"texto": texto})

def crear_curso(request):
    
    formulario = CursoForm()
    
    return render(request, "cursos/crear-curso.html", { "formulario": formulario})