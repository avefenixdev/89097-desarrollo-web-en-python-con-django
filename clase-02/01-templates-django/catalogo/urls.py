from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("producto/<int:producto_id>", views.producto, name="producto"),
    path("lista_productos/", views.lista_productos, name="lista_productos"),
    path("acerca_de", views.acerca, name="acerca_de")
]