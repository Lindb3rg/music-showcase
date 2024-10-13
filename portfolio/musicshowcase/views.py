from django.shortcuts import render
from .models import Composition

def composition_list(request):
    compositions = Composition.objects.all()
    return render(request, 'musicshowcase/composition_list.html', {'compositions': compositions})
