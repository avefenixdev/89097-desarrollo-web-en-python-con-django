from django import forms

class NombreForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=60)