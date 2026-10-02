from django.shortcuts import render
#from django.http import HttpResponse
from .datos import PRODUCTOS

def inicio(request):
    # return HttpResponse("Hola desde Django")
    contexto = {
        "nombre_tienda": "Tiendita de tecnología",
        "mensaje": "Conocé nuestros productos"
    }
    #      render(obj req, plantilla, data)
    return render(request, "catalogo/inicio.html", contexto)

def producto(request):
    contexto = {
        "producto": { "nombre": "Teclado", "precio": 22_000.956, "stock": 10 }
    }
    # Siempre a render() en su tercer argumento le tengo que pasar un dic
    return render(request, "catalogo/producto.html", contexto) 

def lista_productos(request):
    contexto = { "productos": PRODUCTOS }
    return render(request, "catalogo/lista_productos.html", contexto)