from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator

# Model es la representación de nuestro Producto
# El ORM Django ya generar el ID, no necesito explicitamente colocarlo dentro del Modelo
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(black=True) # "" | null=True -> NULL
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.00"))]
    )
    stock = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    
    # toString()
    def __str__(self):
        return self.nombre
