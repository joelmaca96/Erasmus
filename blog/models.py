from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Lugar(models.Model):
    name = models.CharField(max_length=30, unique=True)
    country = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    message = models.TextField()
    img = models.ImageField(upload_to='Places')
    Subimg1 = models.ImageField(upload_to='Places', blank= True)
    Subimg2 = models.ImageField(upload_to='Places', blank=True)
    Subimg3 = models.ImageField(upload_to='Places', blank=True)
    Subimg4 = models.ImageField(upload_to='Places', blank=True)
    created_date = models.DateTimeField(default=timezone.now)
	
    def __str__(self):
 	
        return self.name 
	
	
class Tema(models.Model):
    tema = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    ciudad = models.ForeignKey(Lugar, related_name='temas',on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='temas',on_delete=models.CASCADE)
    message = models.TextField(max_length=4000)
	
class Restaurante(models.Model):
    name = models.CharField(max_length=30, unique=True)
    ciudad = models.ForeignKey(Lugar, related_name='Restaurante',on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255)
    message = models.TextField(max_length=4000)
    img = models.ImageField(upload_to='Places', blank=True)
    Subimg1 = models.ImageField(upload_to='Places', blank=True)
    Subimg2 = models.ImageField(upload_to='Places', blank=True)
    created_by = models.ForeignKey(User, related_name='Restaurante',on_delete=models.CASCADE)
    def __str__(self): 
        return self.name