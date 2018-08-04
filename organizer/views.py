from django.views.generic import View
from django.shortcuts import render
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
    
    def post_valid(self, request):
        from django.http.response import HttpResponse
        return HttpResponse(status=200)

sign_up = Form('sign_up', log_form)
sign_in = SignInForm('sign_in')

log_manager = FormManager(sign_up, sign_in)

class Home(View):
    def get(self, request):
        return render(request, "login.html", {'context':log_manager.window_context})
    
    def post(self, request):
        return log_manager.post(request)