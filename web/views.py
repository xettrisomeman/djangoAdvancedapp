from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import (
    LoginView , 
)
from django.views.generic import (
    TemplateView,
    CreateView  ,
    ListView,
    DetailView
)
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import CustomUser , Post
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


class PostListView(LoginRequiredMixin,ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'web/listview.html'


class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    context_object_name = 'post'
    template_name= 'web/detailview.html'


    def get_object(self, queryset=None):
        return self.model.objects.get(post_id=self.kwargs['post'])


