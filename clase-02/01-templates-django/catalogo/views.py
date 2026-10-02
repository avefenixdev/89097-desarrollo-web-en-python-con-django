from django.shortcuts import render
from django.http import Http404
from .datos import PRODUCTOS

def inicio(request):
    # return HttpResponse("Hola desde Django")
    contexto = {
        "nombre_tienda": "Tiendita de tecnología",
        "mensaje": "Conocé nuestros productos"
    }
    #      render(obj req, plantilla, data)
    return render(request, "catalogo/inicio.html", contexto)

def producto(request, producto_id):
    """  contexto = {
        "producto": { "nombre": "Teclado", "precio": 22_000.956, "stock": 10 }
    } """
    # Obtener los datos de la url del request producto_id
    print(producto_id)
    # Buscamos dentro de la lista PRODUCTOS, el producto del id correspondiente
    for producto in PRODUCTOS:
        if producto["id"] == producto_id:
            contexto = { "producto": producto  }
            return render(request, "catalogo/producto.html", contexto) 

    raise Http404("El producto no existe")
    
def lista_productos(request):
    contexto = { "productos": PRODUCTOS }
    return render(request, "catalogo/lista_productos.html", contexto)

def acerca(request):
    contexto = {
        "titulo_acerca_de": "Acerca de tiendita",
        "mensaje": "Te contamos como empezamos con nuestro emprendimiento"
    }
    return render(request, "catalogo/acerca.html", contexto)