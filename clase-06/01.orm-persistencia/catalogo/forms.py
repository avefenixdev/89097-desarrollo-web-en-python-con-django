from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(
        label="Nombre de producto",
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    descripcion = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control"
            }
        )
    )
    precio = forms.DecimalField(
        max_digits=5, 
        decimal_places=2,
        widget=forms.TextInput(
          attrs={
            "class": "form-control"
          }
        )
    )
    stock = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    
    class Meta: 
        model = Producto
        fields = ["nombre", "descripcion", "precio", "stock"]