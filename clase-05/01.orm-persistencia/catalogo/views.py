from django.shortcuts import render

def listar_productos(request):
    return render(request, "proiductos/lista.html")
def crear_producto(request):
    return render(request, "proiductos/formulario.html")
def detalle_producto(request):
    return render(request, "proiductos/detalle.html")
def editar_producto(request):
    return render(request, "proiductos/formulario.html")
def eliminar_producto(request):
    return render(request, "proiductos/eliminar.html")