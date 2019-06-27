from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .forms import SignUpForm
from .models import CustomUser
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView



class SignUpView(CreateView):
    template_name = 'accounts/signup.html'
    model = CustomUser
    form_class = SignUpForm
    success_url =  reverse_lazy('home')