from django import forms
from django.views.generic import View
from django.shortcuts import render
import json

class LogForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='password', widget=forms.PasswordInput())

class TestView(View):
    def get(self, request):
        context = {
            'log_in': [
                {
                    'type': 'text',
                    'name':'username',
                    'label':'Username',
                }, {
                    'type':'text',
                    'name':'password',
                    'label':'Password',
                },
            ]
        }
        string = json.dumps(context)
        print(string)
        return render(request, "box.html", {'context':repr(string)})
    
    def post(self, request):
        print(request.body)
        form = LogForm(request.POST)
        
        return self.get(request)