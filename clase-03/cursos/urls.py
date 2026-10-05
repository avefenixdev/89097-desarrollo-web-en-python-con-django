from django.urls import path

from . import views

urlpatterns = [
    path("buscar/", views.buscar, name="buscar") # ! http://localhost:8000/cursos/buscar
]