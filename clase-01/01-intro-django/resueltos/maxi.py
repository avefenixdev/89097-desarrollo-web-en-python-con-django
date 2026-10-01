path("horario/", views.horario, name="horario")

def horario(request):
    contenido = """
            <!DOCTYPE html>
            <html lang="es">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Horario de atención</title>
                </head>
                <body>
                    <h1>Horarios de atención<</h1>
                    <p>Lunes a viernes de 9 a 18hs</p>
                    <a href="/">Volver al inicio</a>
                    
                </body>
            </html>
        """
    return HttpResponse(contenido)