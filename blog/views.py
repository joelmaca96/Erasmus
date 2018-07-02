from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from .forms import NewRestaurantForm
from .models import Lugar, Restaurante
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

@login_required
def lugarlist(request):
	lugares = Lugar.objects.order_by('-created_date')[:4]
	return render(request, 'lugares_list.html', {'lugares': lugares})	

@login_required
def Restaurantelist(request, pk):
    lugar= get_object_or_404(Lugar, pk=pk)
    restaurantes = Restaurante.objects.filter(ciudad__name=lugar.name)
	
    return render(request, 'Sitios_list.html', {'restaurantes': restaurantes})
	
@login_required	
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
	
@login_required		
def lugar_topics(request, pk):

    lugar= get_object_or_404(Lugar, pk=pk)
    return render(request, 'temas.html', {'lugar': lugar})
	
@login_required	   
def new_restaurante(request):
    if request.method == 'POST':
        form = NewRestaurantForm(request.POST)

        if form.is_valid():
            restaurante = form.save(commit=False)
            message=form.cleaned_data.get('message')
            restaurante.save()
            return redirect('index')  # TODO: redirect to the created topic page
    else:
        form = NewRestaurantForm()

    return render(request, 'new_Restaurante.html', {'form': form})