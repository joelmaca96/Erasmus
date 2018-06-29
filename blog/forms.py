from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Restaurante

class NewRestaurantForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'placeholder': '¿Por qué te ha gustado?'}), max_length=4000)

    class Meta:
        model = Restaurante
        fields = ['name', 'ciudad', 'direccion', 'message' , 'img']
	
   