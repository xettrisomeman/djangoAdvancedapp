from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import ModelAdmin
from .models import CustomUser  , Post
from .forms import (
    CustomUserAddForm,
    CustomUserChangeForm
)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserAddForm
    form = CustomUserChangeForm
    list_display = ('email' , 'is_staff' , 'is_active')
    list_filter = ('email' , 'is_active')
    fieldsets = (
        (None, {
            "fields": (
                'first_name' , 'last_name','email' , 'password'
            ),
        }),
        (
            'Permissions',{
                'fields':(
                    'is_staff' , 'is_active'
                )
            }
        )
        ,
    )
    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields' : (
                'first_name' , 'last_name','email' , 'password1' , 'password2' , 'is_active','is_staff'
            ),
        }),
    )
    ordering = ('email',)
    search_fields = ('email',)

class CustomPost(ModelAdmin):
    list_display = ('title','post_id')
    list_filter = ('title' ,)
    ordering = ('title',)
    search_fields = ('created_by',)

admin.site.register(Post , CustomPost)


admin.site.register(CustomUser , CustomUserAdmin)

