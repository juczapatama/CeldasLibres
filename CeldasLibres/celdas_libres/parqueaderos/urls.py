from django.urls import path

from .views import CrearTarifa, VerTarifas, EntradaVehiculo

urlpatterns = [
    path('crear_tarifa/', CrearTarifa.as_view(), name='crear_tarifa'),
    path('tarifas/', VerTarifas.as_view(), name='tarifas'),
    path('ingresar-vehiculo/', EntradaVehiculo.as_view(), name='ingresar-vehiculo'),
    # Aca deberia ir la url para el registro de entrada de los vehiculos
]
