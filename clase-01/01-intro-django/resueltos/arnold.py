#views.py
#------------------------------
#Agregar al nav:
#<a href="horarios/">Horarios</a>
#crear def horarios:
def horarios(request):
    contenido = """
        <!DOCTYPE html>
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Horarios</title>
            </head>
            <body>
                <h1>Horarios de atención</h1>
                <p>Lunes a viernes de 9 a 18hs</p>
                <a href="/">Volver al inicio</a>
            </body>
            </html>
    """
    return HttpResponse(contenido)
--------------------------
#urls.py de páginas agregar a urlpatterns:
path("horarios/", views.horarios, name="horarios"),