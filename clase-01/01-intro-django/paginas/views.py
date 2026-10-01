from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# El archivo views de las aplicaciones son función (methods) que devuelve una respuesta o llaman a una plantilla

def inicio(request):
    contenido = """
        <!DOCTYPE html>
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Tiendita</title>
            </head>
            <body>
                <h1>Bienvenidos a Tiendita</h1>
                <p>Este es nuestro primer sitio con Django</p>
                <nav>
                    <a href="acerca/">Acerca de tiendita</a>
                    <a href="contacto/">Contacto</a>
                </nav>
                
            </body>
        </html>
    """
    return HttpResponse(contenido)

def acerca(request):
    contenido = """
            <!DOCTYPE html>
            <html lang="es">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Acerca de Tiendita</title>
                </head>
                <body>
                    <h1>Acerca de Tiendita</h1>
                    <p>Somos una tiendita especializada en IT</p>
                    <a href="/">Volver al inicio</a>
                    
                </body>
            </html>
        """
    return HttpResponse(contenido)

def contacto(request):
    contenido = """
        <!DOCTYPE html>
        <html lang="es">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Contacto</title>
            </head>
            <body>
                <h1>Contacto</h1>
                <p>Correo de ejemplo contacto@gmail.com</p>
                <p>Horario: lunes a viernes de 9 a 18hs</p>
                <a href="/">Volver al inicio</a>
                
            </body>
        </html>
    """
    return HttpResponse(contenido)