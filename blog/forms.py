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
            'nrofono': 'Numero Telefónico',
            'email': 'Correo',
            'colegio': 'Colegio',
            'ciudad': 'Ciudad',
            'aniopost': 'Año',
            'anioegreso': 'Año de Egreso',
            'carrera_post_1': 'Opción 1',
            'carrera_post_2': 'Opción 2',
            'carrera_post_3': 'Opción 3',
        }
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'XXXXXXXX-X'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'nrofono': forms.TextInput(attrs={'placeholder': '+569XXXXXXXX'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'colegio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tu colegio'}),
            'ciudad': forms.Select(attrs={'class': 'form-control'}),
            'aniopost': forms.Select(attrs={'class': 'form-control'}),
            'anioegreso': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:10ch'}),
            'carrera_post_1': forms.Select(attrs={'class': 'form-control'}),
            'carrera_post_2': forms.Select(attrs={'class': 'form-control'}),
            'carrera_post_3': forms.Select(attrs={'class': 'form-control'}),
        }
