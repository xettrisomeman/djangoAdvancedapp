from django.shortcuts import render
from django.contrib.auth.views import (
    LoginView , 
    LogoutView
)
from django.views.generic import TemplateView


from .models import CustomUser
from .forms import (
    CustomUserAddForm,
    UserLoginForm
)


class HomePageView(TemplateView):
    template_name = 'web/homepage.html'


class UserLoginView(LoginView):
    model = CustomUser
    form_class = UserLoginForm
    template_name = 'registration/login.html'


