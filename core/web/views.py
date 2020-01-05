from django.shortcuts import render,redirect , get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.views import (
    LoginView , 
)
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.views.generic import (
    TemplateView,
    CreateView  ,
    ListView,
    DetailView , 
    UpdateView,
    DeleteView,
    FormView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from .models import (
    CustomUser,
    Post,
    Comment
)
from .forms import (
    CustomUserAddForm,
    UserLoginForm,
    PostForm,
    CommentForm
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


# class PostDetailView(LoginRequiredMixin,DetailView):
#     model = Post
#     context_object_name = 'post'
#     template_name= 'webs/detailview.html'


#     def get_object(self, queryset=None):
#         return self.model.objects.get(post_id=self.kwargs['post_id'])


@login_required(redirect_field_name=settings.LOGIN_REDIRECT_URL)
def post_detail_view(request,post_id):
    post = get_object_or_404(Post , post_id=post_id)
    form = CommentForm()
    comments = Comment.objects.filter(post=post)
    datas = {
        'post':post,
        'form':form,
        'comments':comments
    }
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            data = Comment(commented_by=request.user , post=post , comments=form.cleaned_data['comments'])
            data.save()
            messages.add_message(request, messages.INFO, 'Comment has been added')
            return render(request , 'webs/detailview.html' , datas)
    return render(request, 'webs/detailview.html' , datas)





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



