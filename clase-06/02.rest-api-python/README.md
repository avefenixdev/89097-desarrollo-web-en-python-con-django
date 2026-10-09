# Hacer funcionar el panel de administración

## Correr migración que vienen con DJANGO

```sh
py manage.py migrate
```

## Creo el super admin

```sh
py manage.py createsuperuser
```

## Crean una aplicación

```sh
py manage.py startapp cliente
```

## Configuran un modelo básico

> cliente/models.py

```py
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
```

## Activar para aparezca en Admin el cliente

> cliente/admin.py

```py
from .models import Cliente

admin.site.register(Cliente)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "apellido")
```

# Crear el archivo requirements.txt

```sh
py -m pip freeze > requirements.txt
```

# Instalar driver postgres

```sh
py -m pip install "psycopg[binary]"
pip install "psycopg[binary]"
```

## Configuramos Django para que utilice ese motor

> config/settings.py

```py
"default": {
        "ENGINE": "django.db.backends.postgres",
        "NAME": "tienda",
        "USER": "postgres",
        "PASSWORD": "admin",
        "HOST": "localhost",
        "PORT": "5432",
}
```