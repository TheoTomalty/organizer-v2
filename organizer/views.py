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

sign_up = Form('sign_up', log_form)
sign_in = Form('sign_in', log_form)

log_manager = FormManager(sign_up, sign_in)

class Home(View):
    def get(self, request):
        return render(request, "login.html", {'context':log_manager.window_context})
    
    def post(self, request):
        log_manager.post(request)
        
        return self.get(request)