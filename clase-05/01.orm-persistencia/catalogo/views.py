from django.shortcuts import render, redirect
from .forms import ProductoForm
from .models import Producto

def listar_productos(request):
    
    productos = Producto.objects.all().order_by("nombre", "pk")
    return render(request, "productos/lista.html",  { "productos": productos, "titulo": "Listado de productos"})

def crear_producto(request):
    form = ProductoForm(request.POST if request.method == "POST" else None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("productos:lista")
    return render(request, "productos/formulario.html", { "form": form, "titulo": "Nuevo producto" })

def detalle_producto(request, pk):
    return render(request, "productos/detalle.html", { "titulo": "Producto detalle"})
def editar_producto(request, pk):
    return render(request, "productos/formulario.html")
def eliminar_producto(request, pk):
    return render(request, "productos/eliminar.html")