from django.urls import path

from . import views
# urls.py es el archivo de las rutas a la aplicación paginas
urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("acerca/", views.acerca, name="acerca"),
    path("contacto/", views.contacto, name="contacto")
]