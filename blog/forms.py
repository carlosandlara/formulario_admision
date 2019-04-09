from django import forms
from .models import Post, Formulario


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class Form(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = (
            'nombres',
            'apellidos',
            'nrofono',
            'email',
            'colegio',
            'ciudad',
            'carrera_post_1',
            'carrera_post_2',
            'carrera_post_3',
        )
        labels = {
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'nrofono': 'Numero Telefonico',
            'email': 'Correo',
            'colegio': 'Colegio',
            'ciudad': 'Ciudad',
            'carrera_post_1': 'Opción 1',
            'carrera_post_2': 'Opción 2',
            'carrera_post_3': 'Opción 3',
        }
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'nrofono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'colegio': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.Select(attrs={'class': 'form-control'}),
            'carrera_post_1': forms.Select(attrs={'class': 'form-control'}),
            'carrera_post_2': forms.Select(attrs={'class': 'form-control'}),
            'carrera_post_3': forms.Select(attrs={'class': 'form-control'}),
        }
