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