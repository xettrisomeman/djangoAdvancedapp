from django.shortcuts import render,redirect
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
from django.contrib.messages.views import SuccessMessageMixin

from .models import CustomUser , Post
from .forms import (
    CustomUserAddForm,
    UserLoginForm,
    PostForm
)


class HomePageView(LoginRequiredMixin,TemplateView):
    template_name = 'webs/homepage.html'


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
    template_name = 'webs/listview.html'

    def get_queryset(self):
        return self.model.objects.all().order_by('title')


class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    context_object_name = 'post'
    template_name= 'webs/detailview.html'


    def get_object(self, queryset=None):
        return self.model.objects.get(post_id=self.kwargs['post'])


class PostCreateView(SuccessMessageMixin,LoginRequiredMixin , CreateView):
    model = Post
    form_class = PostForm
    template_name = 'webs/postview.html'
    success_url = reverse_lazy('list')
    success_message = 'Post has been created'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.save()
        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        kwargs['data'] = 'add'
        return super().get_context_data(**kwargs)


class PostUpdateView(SuccessMessageMixin,LoginRequiredMixin , UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'webs/postview.html'
    success_url = reverse_lazy('list')
    success_message = 'Post has been updated'

    def dispatch(self, request, *args, **kwargs):
        if request.user.email != self.get_object().created_by.email :
            return redirect(reverse_lazy('list'))
        return super().dispatch(request ,*args,**kwargs)

    def get_object(self, queryset=None):
        return self.model.objects.get(post_id=self.kwargs['post_id'])

    def get_context_data(self, **kwargs):
        kwargs['data'] = 'update'
        return super().get_context_data(**kwargs)


class PostDeleteView(SuccessMessageMixin,LoginRequiredMixin,DeleteView):
    model = Post
    template_name = 'webs/postdelete.html'
    success_url = reverse_lazy('list')
    context_object_name = 'post'

    def dispatch(self, request, *args, **kwargs):
        if request.user.email != self.get_object().created_by.email :
            return redirect(reverse_lazy('list'))
        return super().dispatch(request ,*args,**kwargs)

    def get_object(self, queryset=None):
        return self.model.objects.get(post_id=self.kwargs['post_id'])

