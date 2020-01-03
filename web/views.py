from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import (
    LoginView , 
)
from django.views.generic import (
    TemplateView,
    CreateView
)
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import CustomUser
from .forms import (
    CustomUserAddForm,
    UserLoginForm
)


class HomePageView(LoginRequiredMixin,TemplateView):
    template_name = 'web/homepage.html'


class UserLoginView(LoginView):
    model = CustomUser
    form_class = UserLoginForm
    template_name = 'registration/login.html'



class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserAddForm
    template_name='registration/signup.html'
    success_url = reverse_lazy('login')

