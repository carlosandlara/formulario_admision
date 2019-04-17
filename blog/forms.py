from django import forms
from .models import Post, Formulario
"""from phonenumber_field.formfields import PhoneNumberField"""


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class Form(forms.ModelForm):
    class Meta:
        model = Formulario

        fields = (
            'rut',
            'nombres',
            'apellidos',
            'nrofono',
            'email',
            'colegio',
            'ciudad',
            'colegioadv',
            'aniopost',
            'anioegreso',
            'carrera_post_1',
            'carrera_post_2',
            'carrera_post_3',
        )
        labels = {
            'rut': 'RUT',
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'nrofono': 'Número Telefónico',
            'email': 'Correo',
            'colegio': 'Colegio',
            'ciudad': 'Ciudad',
            'colegioadv': 'Colegio Adventista',
            'aniopost': 'Curso',
            'anioegreso': 'Año de Egreso',
            'carrera_post_1': 'Opción 1',
            'carrera_post_2': 'Opción 2',
            'carrera_post_3': 'Opción 3',
        }

        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'XXXXXXXXX'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'nrofono': forms.TextInput(attrs={'placeholder': '9XXXXXXXX'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'colegio': forms.Select(attrs={'class': 'form-control'}),
            'ciudad': forms.Select(attrs={'class': 'form-control'}),
            'colegioadv': forms.Select(attrs={'class': 'form-control'}),
            'aniopost': forms.Select(attrs={'class': 'form-control'}),
            'anioegreso': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:10ch'}),
            'carrera_post_1': forms.Select(attrs={'class': 'form-control'}),
            'carrera_post_2': forms.Select(attrs={'class': 'form-control'}),
            'carrera_post_3': forms.Select(attrs={'class': 'form-control'}),
        }
