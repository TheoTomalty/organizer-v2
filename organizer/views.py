from django.views.generic import View
from django.shortcuts import render

class TestView(View):
    def get(self, request):
        return render(request, "test.html")