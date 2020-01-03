from django import forms

from django.contrib.auth.forms import (
    UserChangeForm,
    UserCreationForm,
    AuthenticationForm
)
from .models import CustomUser


class CustomUserAddForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


