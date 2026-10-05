from django.shortcuts import render

def buscar(request):
    texto = request.GET.get("q", "")
    return render(request, "cursos/buscar.html", {"texto": texto})

def crear_curso(request):
    return render(request, "cursos/crear-curso.html")