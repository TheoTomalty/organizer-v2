from django.views.generic import View
from django.shortcuts import render
from organizer.forms import Form, FormManager

class Home(View):
    def get(self, request):
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
        
        context = FormManager(sign_up, sign_in).window_context
        
        return render(request, "login.html", {'context':context})
    
    def post(self, request):
        print(request.body)
        
        return self.get(request)