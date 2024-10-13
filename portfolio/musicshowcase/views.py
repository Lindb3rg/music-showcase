from django.shortcuts import render
from .models import Composition, Service

def composition_list(request):
    compositions = Composition.objects.all()
    return render(request, 'musicshowcase/composition_list.html', {'compositions': compositions})

def components(request):
    return render(request, 'musicshowcase/components.html', {})

def index(request):
    
    compositions = Composition.objects.all()
    services = Service.objects.all()
    
    unique_genres = Composition.objects.values_list('genre', flat=True).distinct()
    genres_dict = {genre: genre.replace('_', ' ') for genre in unique_genres}
    
    



    context = {
        'compositions': compositions,
        'genres_dict': genres_dict,
        'services': services,
    }
    
    
    return render(request, 'musicshowcase/index.html', context)