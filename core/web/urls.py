from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views


urlpatterns = [
    path('' , views.HomePageView.as_view() , name='homepage'),
    path('accounts/login/' , views.UserLoginView.as_view() ,name='login'),
    path('accounts/signup/' , views.SignUpView.as_view() ,name='signup'),
    path('list/' , views.PostListView.as_view() ,name='list'),
    path('list/<uuid:post>/' , views.PostDetailView.as_view() ,name='detailview'),
    path('list/create/' , views.PostCreateView.as_view() , name='create'),
    path('list/update/<uuid:post_id>/' , views.PostUpdateView.as_view() , name='update'),
    path('list/delete/<uuid:post_id>/' , views.PostDeleteView.as_view() , name='delete'),
    

]
