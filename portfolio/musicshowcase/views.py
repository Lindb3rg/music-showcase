from django.shortcuts import render
from .models import Composition

def composition_list(request):
    compositions = Composition.objects.all()
    return render(request, 'music/composition_list.html', {'compositions': compositions})
