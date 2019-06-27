from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .forms import SignUpForm
from .models import CustomUser
from django.urls import reverse_lazy
from django.views.generic.edit import FormView



class SignUpView(FormView):
    template_name = 'accounts/signup.html'
    model = CustomUser
    form_class = SignUpForm
    success_url =  reverse_lazy('home')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})