from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    
    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'
    
    
    def __str__(self):
        return self.titulo
    
    