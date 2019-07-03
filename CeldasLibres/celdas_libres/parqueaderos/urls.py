from django.urls import path

from .views import CrearTarifa, VerTarifas, CrearEntradaVehiculo, VerIngresados

urlpatterns = [
    path('crear_tarifa/', CrearTarifa.as_view(), name='crear_tarifa'),
    path('tarifas/', VerTarifas.as_view(), name='tarifas'),
    path('ingresar-vehiculo/', CrearEntradaVehiculo.as_view(), name='ingresar-vehiculo'),
    path('vehiculos-ingresados/', VerIngresados.as_view(), name='vehiculos-ingresados'),
]
