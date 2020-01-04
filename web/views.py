from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import (
    LoginView , 
)
from django.views.generic import (
    TemplateView,
    CreateView  ,
    ListView,
    DetailView , 
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import CustomUser , Post
from .forms import (
    CustomUserAddForm,
    UserLoginForm,
    PostForm
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


class PostCreateView(LoginRequiredMixin , CreateView):
    model = Post
    form_class = PostForm
    template_name = 'web/postview.html'
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.save()
        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        kwargs['data'] = 'add'
        return super().get_context_data(**kwargs)


class PostUpdateView(LoginRequiredMixin , UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'web/postview.html'
    success_url = reverse_lazy('list')

    def get_object(self, queryset=None):
        return self.model.objects.get(post_id=self.kwargs['post_id'])

    def get_context_data(self, **kwargs):
        kwargs['data'] = 'update'
        return super().get_context_data(**kwargs)

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'web/postdelete.html'
    success_url = reverse_lazy('list')
    context_object_name = 'post'


    def get_object(self, queryset=None):
        return self.model.objects.get(post_id=self.kwargs['post_id'])

