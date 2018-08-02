from django.views.generic import View
from django.shortcuts import render
from organizer.forms import Form
import re

def LogForm(name):
    return Form(name, {
            'username': {
                'type': 'text',
                'label': 'Username',
            },
            'password': {
                'type': 'text',
                'label': 'Password',
            },
        })

class TestView(View):
    def get(self, request):
        form = LogForm('sign_in')
        
        return render(request, "box.html", {'context':form.html})
    
    #def post(self, request):
    #    print(request.body)
    #    form = LogForm(request.POST)
    #    
    #    return self.get(request)