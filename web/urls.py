from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views


urlpatterns = [
    path('' , views.HomePageView.as_view() , name='homepage'),
    path('accounts/login/' , views.UserLoginView.as_view() ,name='login'),
    path('accounts/signup/' , views.SignUpView.as_view() ,name='signup'),
    path('list/' , views.PostListView.as_view() ,name='list'),
    path('list/<uuid:post>/' , views.PostDetailView.as_view() ,name='detailview'),
    
    
]
