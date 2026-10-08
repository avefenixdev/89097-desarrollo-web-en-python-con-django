from django.shortcuts import render

def listar_productos(request):
    return render(request, "productos/lista.html")
def crear_producto(request):
    return render(request, "productos/formulario.html")
def detalle_producto(request, pk):
    return render(request, "productos/detalle.html")
def editar_producto(request, pk):
    return render(request, "productos/formulario.html")
def eliminar_producto(request, pk):
    return render(request, "productos/eliminar.html")