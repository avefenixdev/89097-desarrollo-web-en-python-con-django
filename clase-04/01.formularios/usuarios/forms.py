from django import forms

class UsuarioForm(forms.Form):
    nombre = forms.CharField(
        label="Nombre y apellido",
        min_length=3,
        max_length=60,
        help_text="Ingrese su nombre y apellido",
        error_messages={"required": "Completá tu nombre y apellido."},
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Escriba su nombre aquí"
            }
        )
    )
    email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Escriba su nombre aquí"
        }
    )
    )
    edad = forms.IntegerField(
        label="Edad", 
        min_value=16, 
        max_value=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ingrese la edad"
            }
        )
    )
    curso = forms.ChoiceField(
        label="Curso",
        choices=[("python", "Python inicial"), ("django", "Django inicial")],
        widget=forms.Select(
            attrs={
                "class": "form-select"
            }
        )
    )
    experiencia = forms.ChoiceField(
        label="Experiencia previa",
        choices=[
            ('ninguna', "Sin experiencia"),
            ('basica', "Conocimiento básicos de Python"),
        ],
        widget=forms.Select(
            attrs={
                "class": "form-select"
            }
        )
    )
    comentario = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Escriba su comentario por favor"
            }
        )
    )
    # Validación individual del input nombre
    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        if len(nombre.split()) > 2:
            raise forms.ValidationError("Escribí tu y apellido")
        return nombre
    # Validación combinada entre curso y experiencia
    def clean(self):
        datos = super().clean()
        curso = datos.get("curso")
        experiencia = datos.get("experiencia")
        if curso == "django" and experiencia == "ninguna":
            raise forms.ValidationError(
                "Para aprender DJANGO necesitas conocimiento básicos de Python"
            )
        return datos