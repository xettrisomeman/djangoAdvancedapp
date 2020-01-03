from django.shortcuts import render
from django.contrib.auth.views import (
    LoginView , 
)
from django.views.generic import TemplateView
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



