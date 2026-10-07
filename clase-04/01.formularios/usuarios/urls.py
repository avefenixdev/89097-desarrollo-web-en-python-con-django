from django.urls import path

from . import views

app_name = "usuarios"

urlpatterns = [
    path("formulario/", views.crear_usuario, name="crear-usuario"),
    path("mensaje/", views.confirmacion, name="confirmacion"),
]