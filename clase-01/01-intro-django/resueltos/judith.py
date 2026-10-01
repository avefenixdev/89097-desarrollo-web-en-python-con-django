from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def inicio(request):

    contenido = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Inicio - Tiendita</title>
    </head>
    <body>

        <header>
            <h1>Bienvenidos a Tiendita</h1>
            <p>Tu tienda especializada en productos</p>
        </header>

        <nav>
            <ul>
                <li><a href="/">Inicio</a></li>
                <li><a href="/acerca/">Acerca de</a></li>
                <li><a href="/contacto/">Contacto</a></li>
                <li><a href="/horarios/">Horarios</a></li>
            </ul>
        </nav>

        <main>
            <section>
                <h2>Bienvenidos a nuestro sitio</h2>
                <p>
                    Este es nuestro primer sitio web desarrollado utilizando Django.
                    Estamos aprendiendo a crear aplicaciones web y a conectar
                    diferentes páginas mediante rutas.
                </p>
            </section>

            <section>
                <h2>¿Qué podés encontrar en Tiendita?</h2>
                <ul>
                    <li>Productos tecnológicos</li>
                    <li>Accesorios para computadoras</li>
                    <li>Componentes informáticos</li>
                    <li>Elementos para el hogar y la oficina</li>
                </ul>
            </section>

            <section>
                <h2>Novedades</h2>
                <p>
                    Próximamente incorporaremos nuevos productos y servicios
                    para nuestros clientes
                </p>
            </section>
        </main>

        <footer>
            <p>&copy; 2026 Tiendita. Todos los derechos reservados.</p>
        </footer>

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

        <header>
            <h1>Acerca de Tiendita</h1>
            <p>Conocé un poco más sobre nuestro negocio</p>
        </header>

        <nav>
            <ul>
                <li><a href="/">Inicio</a></li>
                <li><a href="/acerca/">Acerca de</a></li>
                <li><a href="/contacto/">Contacto</a></li>
                <li><a href="/horarios/">Horarios</a></li>
            </ul>
        </nav>

        <main>
            <section>
                <h2>¿Quiénes somos?</h2>
                <p>
                    Somos una tiendita especializada en vender productos que solo encontrarás en TIendita
                </p>

                <p>
                    Nuestro objetivo es ofrecer productos útiles y accesibles
                    para estudiantes, profesionales y personas interesadas
                    en el mundo entero
                </p>
            </section>

            <section>
                <h2>Nuestra misión</h2>
                <p>
                    Buscamos brindar una atención cercana y ayudar a nuestros
                    clientes a encontrar los productos que necesitan.
                </p>
            </section>

            <section>
                <h2>¿Por qué elegirnos?</h2>
                <ul>
                    <li>Atención personalizada</li>
                    <li>Productos tecnológicos</li>
                    <li>Precios accesibles</li>
                    <li>Asesoramiento a nuestros clientes</li>
                </ul>
            </section>
        </main>

        <p><a href="/">Volver al inicio</a></p>

        <footer>
            <p>&copy; 2026 Tiendita. Todos los derechos reservados.</p>
        </footer>

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

        <header>
            <h1>Contacto</h1>
            <p>Estamos disponibles para responder tus consultas.</p>
        </header>

        <nav>
            <ul>
                <li><a href="/">Inicio</a></li>
                <li><a href="/acerca/">Acerca de</a></li>
                <li><a href="/contacto/">Contacto</a></li>
                <li><a href="/horarios/">Horarios</a></li>
            </ul>
        </nav>

        <main>
            <section>
                <h2>Datos de contacto</h2>

                <p>
                    <strong>Correo electrónico:</strong>
                    contacto@gmail.com
                </p>

                <p>
                    <strong>Teléfono:</strong>
                    11-1234-5678
                </p>

                <p>
                    <strong>Dirección:</strong>
                    Avenida Siempre Viva 123
                </p>
            </section>

            <section>
                <h2>Atención al cliente</h2>
                <p>
                    Podés comunicarte con nosotros para realizar consultas
                    sobre productos, disponibilidad y horarios de atención.
                </p>

                <p>
                    Respondemos las consultas dentro de nuestro horario
                    habitual de atención.
                </p>
            </section>

            <section>
                <h2>Horario de atención</h2>
                <p>
                    Lunes a viernes de 9:00 a 18:00 hs.
                </p>
            </section>
        </main>

        <p><a href="/">Volver al inicio</a></p>

        <footer>
            <p>&copy; 2026 Tiendita. Todos los derechos reservados.</p>
        </footer>

    </body>
    </html>
    """

    return HttpResponse(contenido)


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

        <header>
            <h1>Horarios de atención</h1>
            <p>Consultá nuestros días y horarios de atención.</p>
        </header>

        <nav>
            <ul>
                <li><a href="/">Inicio</a></li>
                <li><a href="/acerca/">Acerca de</a></li>
                <li><a href="/contacto/">Contacto</a></li>
                <li><a href="/horarios/">Horarios</a></li>
            </ul>
        </nav>

        <main>
            <section>
                <h2>Horarios habituales</h2>

                <ul>
                    <li>Lunes: 9:00 a 18:00 hs</li>
                    <li>Martes: 9:00 a 18:00 hs</li>
                    <li>Miércoles: 9:00 a 18:00 hs</li>
                    <li>Jueves: 9:00 a 18:00 hs</li>
                    <li>Viernes: 9:00 a 18:00 hs</li>
                    <li>Sábado: 10:00 a 14:00 hs</li>
                    <li>Domingo: Cerrado</li>
                </ul>
            </section>

            <section>
                <h2>Información importante</h2>
                <p>
                    Los horarios pueden modificarse durante feriados
                    o fechas especiales.
                </p>

                <p>
                    Para confirmar nuestra disponibilidad, podés
                    comunicarte con nosotros a través de la sección
                    de contacto.
                </p>
            </section>
        </main>

        <p><a href="/">Volver al inicio</a></p>

        <footer>
            <p>&copy; 2026 Tiendita. Todos los derechos reservados.</p>
        </footer>

    </body>
    </html>
    """

    return HttpResponse(contenido)


# En urls.py de la carpeta "paginas"
path("horarios/", views.horarios, name="horarios")