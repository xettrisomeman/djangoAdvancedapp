from django.shortcuts import reverse, HttpResponseRedirect


#custom middleware
def login_register_middleware(get_response):
    def middleware(request):
       login_path = '/accounts/login/'
       register_path = '/accounts/signup/'
       print(request.path)
       if request.user.is_authenticated and (request.path == login_path or request.path==register_path):
           return HttpResponseRedirect(reverse('homepage'))
       return get_response(request)
    return middleware








