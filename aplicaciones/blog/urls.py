from django.urls import path
from . import views

urlpatterns = [
    path('',views.blogListView.as_view(), name='Blog'),
   
]
