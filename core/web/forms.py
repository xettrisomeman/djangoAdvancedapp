from django import forms

from django.contrib.auth.forms import (
    UserChangeForm,
    UserCreationForm,
    AuthenticationForm
)
from .models import (
    CustomUser,
    Post,
    Comment
)


class CustomUserAddForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('first_name' , 'last_name','email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','email')


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = CustomUser
        fields = "__all__"

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title' , 'content')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comments',)

