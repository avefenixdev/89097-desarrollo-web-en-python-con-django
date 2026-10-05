from django.urls import path

from . import views

app_name = "cursos"

urlpatterns = [
    path("buscar/", views.buscar, name="buscar"), # ! http://localhost:8000/cursos/buscar
    path("crear-curso/", views.crear_curso, name="crear-curso")
]