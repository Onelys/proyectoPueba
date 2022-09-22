from django.urls import path
from . import views

urlpatterns = [
    path('',views.BlogList.as_view(), name='Blog'),
    path('create/',views.BlogCreate.as_view(), name='Create'),
    path('editar/<int:pk>/',views.BlogUpdate.as_view(), name='Editar'),
    path('eliminar/<int:pk>/',views.BlogDelete.as_view(), name='Eliminar'),
   
]
