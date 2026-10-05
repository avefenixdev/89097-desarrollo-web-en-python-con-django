from django import forms

class CursoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=60)
    categoria = forms.CharField(label="Categoría", max_length=30)