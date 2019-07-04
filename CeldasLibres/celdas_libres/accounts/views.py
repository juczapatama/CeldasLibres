from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .forms import SignUpForm
from .models import CustomUser
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib import messages


class SignUpView(CreateView):
    template_name = 'accounts/signup.html'
    model = CustomUser
    form_class = SignUpForm
    success_url =  reverse_lazy('home')


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            user.usuario.identificacion = form.cleaned_data['username']
            user.usuario.tipo_identificacion = form.cleaned_data['tipo_identificacion']
            user.usuario.nacionalidad = form.cleaned_data['nacionalidad']
            user.usuario.fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            user.usuario.telefono = form.cleaned_data['telefono']
            user.usuario.celular = form.cleaned_data['celular']
            user.usuario.direccion = form.cleaned_data['direccion']
            user.save()
            messages.success(request, 'Registro exitoso')
            return redirect('home')
        return render(request, 'accounts/signup.html', {'form': form})
