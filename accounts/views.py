from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login') #lazy перенаправит только после заполнения форм, простой reverse - сразу 
    template_name = 'accounts/signup.html' #accounts - это название приложения!