from django.views.generic import View
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from organizer.forms import Form, FormManager

log_form = {
    'username': {
        'type': 'text',
        'label': 'Username',
    },
    'password': {
        'type': 'password',
        'label': 'Password',
    },
}

class SignInForm(Form):
    def __init__(self, name):
        super().__init__(name, log_form)
    
    def post_valid(self, request, form):
        data = self.clean_data(form)
        user = authenticate(request, **data)
        
        if user is not None:
            login(request, user)
            return render(request, 'login.html', {'context':self.manager.window_context})
        else:
            from django.http.response import HttpResponse
            return HttpResponse(status=401)

class SignUpForm(Form):
    def __init__(self, name):
        super().__init__(name, log_form)

    def post_valid(self, request, form):
        data = self.clean_data(form)

        if User.objects.filter(username=data['username']).exists():
            raise NotImplementedError('Must implement form error handling')
        else:
            user = User.objects.create_user(**data)
            user.backend = settings.AUTHENTICATION_BACKENDS[0]
            login(request, user)
            return render(request, 'login.html', {'context':self.manager.window_context})

sign_up = SignUpForm('sign_up')
sign_in = SignInForm('sign_in')

log_manager = FormManager(sign_up, sign_in)

class Home(View):
    def get(self, request):
        return render(request, "login.html", {'context':log_manager.window_context})
    
    def post(self, request):
        return log_manager.post(request)