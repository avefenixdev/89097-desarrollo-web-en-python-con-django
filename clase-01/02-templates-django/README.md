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