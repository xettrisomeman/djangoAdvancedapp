from django.urls import path


from . import views


urlpatterns = [
    path('' , views.HomePageView.as_view() , name='homepage'),
    path('login/' , views.UserLoginView.as_view() ,name='login'),
    
]
