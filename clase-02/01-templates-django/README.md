# Verificiar plantillas activas en Apps
Es importante verificar que tengo activa la posibilidad de tener plantillas dentro de las Apps (módulos)

> config/settings.py

```py
TEMPLATES = [
    {
        "DIRS": [], # puedo rutas especificas
        "APP_DIRS": True, # habilito la posibilidad de tener plantillas dentro de las App
    },
]
``` 

# Template de .gitignore

<https://gist.github.com/santoshpy/6f982faf1eacdac153ffd86a3a694239>

# Trabajando con el template

```html
<h1>{{ ... }}</h1> <!-- Mostrar un valor -->
<div>{% ... %}</div> <!-- Ejecutar una etiqueta de plantilla -> {% if producto.stock > 0 %} -->
{# ... #} <!-- comentario de plantilla  -->
```

# En las plantilla tenemos filtros

* upper
* floatformat:2

```html
<p>Precio: ${{ producto.precio|floatformat:2 }}</p>
```