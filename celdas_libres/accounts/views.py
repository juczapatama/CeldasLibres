from django.shortcuts import render

from .forms import SignUpForm
from django.views.generic.edit import FormView

class SignUpView(FormView):
    template_name = 'signup.html'
    form_class = SignUpForm
