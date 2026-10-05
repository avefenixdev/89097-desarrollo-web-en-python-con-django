from django import forms

class UsuarioForm(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    edad = forms.IntegerField()
    """ curso = forms.ChoiceField()
    experiencia = forms.ChoiceField() """
    comentario = forms.CharField()