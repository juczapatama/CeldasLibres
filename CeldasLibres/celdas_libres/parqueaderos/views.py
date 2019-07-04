from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .models import Tarifa, EntradaVehiculo
from .forms import CrearTarifaForm, EntradaVehiculoForm
from django.contrib import messages


@method_decorator([login_required, staff_member_required], name='dispatch')
class CrearTarifa(CreateView):
    model = Tarifa
    template_name = 'parqueaderos/crear_tarifa.html'
    form_class = CrearTarifaForm
    success_url = reverse_lazy('tarifas')
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            messages.success(request, 'Tarifa creada')
        return super(CrearTarifa, self).post(request, kwargs)



@method_decorator([login_required], name='dispatch')
class VerTarifas(ListView):
    model = Tarifa
    context_object_name = 'tarifas_list'
    template_name = 'parqueaderos/tarifas.html'

@method_decorator([login_required], name='dispatch')
class CrearEntradaVehiculo(CreateView):
    model = EntradaVehiculo
    template_name = 'parqueaderos/ingresar_vehiculo.html'
    form_class = EntradaVehiculoForm
    success_url = reverse_lazy('vehiculos-ingresados')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            messages.success(request, 'Vehículo ingresado')
        return super(CrearEntradaVehiculo, self).post(request, kwargs)

@method_decorator([login_required], name='dispatch')
class VerIngresados(ListView):
    model = EntradaVehiculo
    context_object_name = 'ingresados_list'
    template_name = 'parqueaderos/ingresados_list.html'