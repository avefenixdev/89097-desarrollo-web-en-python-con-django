from django.shortcuts import render, redirect, get_object_or_404
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
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, "productos/detalle.html", { "producto": producto, "titulo": "Producto detalle"})

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    form = ProductoForm(request.POST if request.method == "POST" else None, instance=producto)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("productos:lista")
    return render(request, "productos/formulario.html", { "form": form, "titulo": "Editando producto"})
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        producto.delete()
        return redirect("productos:lista")
    return render(request, "productos/eliminar.html", { "producto": producto, "titulo": "Eliminando producto"})