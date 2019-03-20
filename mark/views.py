from django.shortcuts import render

# Create your views here.
from django.views import View


class MarkCountView(View):
    def get(self,request, *args, **kwargs):
        print("hello")
        return render(request, "Hello World")