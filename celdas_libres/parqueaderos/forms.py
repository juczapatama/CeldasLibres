from django import forms
from .models import Tarifa


class CrearTarifaForm(forms.ModelForm):
    tipo_vehiculo = forms.ChoiceField(
        choices=[
            ('carro', 'Carro'),
            ('moto', 'Moto'),
        ],
    )

    class Meta:
        model = Tarifa
        fields = '__all__'
        widgets = {
            'anno': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tipo_vehiculo': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'por_hora': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class EntradaVehiculoForm(forms.ModelForm):
    pass
    # Formulario para el registro de entrada de vehiculos
    # Ver modelo para los campos