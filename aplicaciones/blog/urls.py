from django.urls import path
from . import views

urlpatterns = [
    path('',views.blogListView.as_view(), name='Blog'),
    path('create/',views.blogCreateView.as_view(), name='Create'),
   
]
