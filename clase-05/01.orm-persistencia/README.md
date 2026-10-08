# Clase 05

## Crear el archivo de migraciones a partir del modelo

```sh
py manage.py makemigrations catalogo
```

> Se generar archivos dentro de la carpeta 'migrations' de la app 'catalogo'

A medida que voy modificando el modelo tengo que volver a correr el makemigrations la estructura de archivos generada

```
0001_initial.py
0002_producto_marca.py
000x_modificacion_incremental_del_modelo.py
```

> Todo esto no modifica la base de datos

## Para impactar las migraciones en la DB tengo que correr la migraciones

```sh
py manage.py migrate
``` 

## .gitignore

<https://gist.github.com/santoshpy/6f982faf1eacdac153ffd86a3a694239>


```py
from decimal import Decimal
>>> from catalogo.models import Producto
>>> teclado = Producto(
...     nombre="Teclado",
...     descripcion="Teclado USB",
...     precio=Decimal("25000.00"),
...     stock=10 
... )
>>> print(teclado.pk)
None
>>> teclado.full_clean()
>>> teclado.save()
>>> print(teclado.pk)
1
>>> print(teclado)
Teclado
>>> mouse = Producto.objects.create(
...     nombre="Mouse",
...     marca="Microsoft",
...     precio=Decimal("12000.00"),
...     stock=5
... )
>>> print(mouse.pk)
2
``` 