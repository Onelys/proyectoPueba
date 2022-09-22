from ast import arg
from msilib.schema import ListView
from venv import create
from django.shortcuts import render, redirect
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from . forms import BlogCreateForm
from . models import Post
from django.urls import reverse_lazy

# Create your views here.


        
class BlogList(ListView):
    model = Post
    template_name = 'blog.html'
    
class BlogCreate(CreateView):
    model = Post
    form_class = BlogCreateForm
    template_name = 'blog_create.html'
    success_url = reverse_lazy('Index')
    
class BlogUpdate(UpdateView):
    model = Post
    form_class = BlogCreateForm
    template_name = 'blog_create.html'
    success_url = reverse_lazy('Blog')

class BlogDelete(DeleteView):
    model = Post
    template_name = 'verificacion.html'
    success_url = reverse_lazy('Blog')
    
    
'''class blogListView(View):
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
        return render(request, 'blog_create.html', contexto)'''

