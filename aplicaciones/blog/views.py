from ast import arg
from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class blogListView(View):
    def get(self,request,*args, **kwargs):
        contexto={
            
        }
        return render(request, 'blog.html', contexto)
