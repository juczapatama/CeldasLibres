from django.urls import path

from .views import CrearTarifa, VerTarifas

urlpatterns = [
    path('crear_tarifa/', CrearTarifa.as_view(), name='crear_tarifa'),
    path('tarifas/', VerTarifas.as_view(), name='tarifas'),
]
