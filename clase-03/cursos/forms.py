from django import forms

class CursoForm(forms.Form):
    # atributos
    nombre = forms.CharField(
        label="Nombre", 
        max_length=60
    )
    categoria = forms.CharField(
        label="Categoría", 
        max_length=30
    )
    experiencia = forms.CharField(
        label="Experiencia",
        max_length=30
    )
    # métodos (Validación de campo)
    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        if len(nombre.split()) < 2: 
            raise forms.ValidationError('Escribí un nombre descriptivo')
        return nombre
    
    def clean(self):
        datos = super().clean()
        nombre = datos.get("nombre")
        experiencia = datos.get("experiencia")
        if nombre is not None and "django" in nombre and experiencia != "python":
            raise forms.ValidationError(
                "Para poder realizar el curso de Django es necesario tener experiencia en Python"
            )
        return datos
    