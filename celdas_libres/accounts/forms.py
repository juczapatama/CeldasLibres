from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class SignUpForm(UserCreationForm):
    nombre1 = forms.CharField(
        label='Primer nombre', max_length=50, required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Pepito', 'autofocus': 'autofocus'}
        )
    )
    nombre2 = forms.CharField(
        label='Segundo nombre', max_length=50, required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Javier', 'autofocus': 'autofocus'}
        )
    )
    apellido1 = forms.CharField(
        label='Primer apellidos', max_length=50, required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Perez'}
        )
    )
    apellido2 = forms.CharField(
        label='Segundo apellidos', max_length=50, required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Lopez'}
        )
    )
    # Username es con lo que se va a logear, que en este caso lo vamos a tratar como la identificacion
    username = forms.EmailField(
        label='Identificacion', required=True,
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}
        )
    )
    password1 = forms.CharField(
        label='Contraseña', required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    password2 = forms.CharField(
        label='Verificar contraseña', required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    email = forms.EmailField(
        label='Correo electrónico', required=False,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Correo electrónico'
                }
        )
    )
    tipo_identificacion = forms.ChoiceField(
        required=True,
        choices=[
            ('TI', 'Tarjeta de identidad'),
            ('CC', 'Cédula de ciudadanía'),
            ('CE', 'Cédula de extranjería'),
        ]
    )
    nacionalidad = forms.CharField(max_length=15)
    fecha_nacimiento = forms.DateField(input_formats=['%d/%m/%Y'])
    telefono = forms.CharField(max_length=15)
    celular = forms.CharField(max_length=15)
    direccion = forms.CharField(max_length=30)

    class Meta:
        model = CustomUser
        fields = [
            'nombre1', 'nombre2', 'apellido1', 'apellido2', 'username',
            'password1', 'password2', 'email', 'tipo_identificacion',
            'nacionalidad', 'fecha_nacimiento', 'telefono', 'celular',
            'direccion',
            ]
