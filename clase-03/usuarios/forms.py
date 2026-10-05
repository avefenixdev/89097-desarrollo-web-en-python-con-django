from django import forms

class UsuarioForm(forms.Form):
    nombre = forms.CharField(
        label="Nombre y apellido",
        min_length=3,
        max_length=60,
        help_text="Ingrese su nombre y apellido",
        error_messages={"required": "Completá tu nombre y apellido."}
    )
    email = forms.EmailField(label="Correo electrónico")
    edad = forms.IntegerField(label="Edad", min_value=16, max_value=100)
    curso = forms.ChoiceField(
        label="Curso",
        choices=[("python", "Python inicial"), ("django", "Django inicial")]
    )
    """ experiencia = forms.ChoiceField() """
    comentario = forms.CharField()