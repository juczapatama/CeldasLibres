from django.contrib import admin

from .forms import CrearTarifaForm
from .models import Tarifa


class TarifaAdmin(admin.ModelAdmin):
    model = Tarifa
    list_display = ['anno', 'tipo_vehiculo', 'por_hora']

admin.site.register(Tarifa, TarifaAdmin)
