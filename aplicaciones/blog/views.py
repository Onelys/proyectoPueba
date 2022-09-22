from ast import arg
from venv import create
from django.shortcuts import render, redirect
from django.views.generic import View
from . forms import BlogCreateForm
from . models import Post

# Create your views here.

class blogListView(View):
    def get(self,request,*args, **kwargs):
        contexto={
            
        }
        return render(request, 'blog.html', contexto)
    
class blogCreateView(View):
    def get(self,request,*args, **kwargs):     
        form = BlogCreateForm()
        contexto = {
            'form': form      
        }
        return render(request, 'blog_create.html', contexto)
    
    def post(self,request,*args, **kwargs):
        if request.method=="POST":
            form = BlogCreateForm(request.POST)
            if form.is_valid():
                titulo = form.cleaned_data.get('titulo')
                contenido = form.cleaned_data.get('contenido')
                p, created = Post.objects.get_or_create(titulo=titulo, contenido=contenido)
                p.save()
                return redirect('Blog')
        contexto={
            
        }
        return render(request, 'blog_create.html', contexto)


