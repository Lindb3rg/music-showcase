from django.shortcuts import render,redirect
from .models import Composition, Service
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

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
    
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_message = f"Message from {name} ({email}):\n\n{message}"

            # Send email
            send_mail(subject, full_message, email, [settings.DEFAULT_FROM_EMAIL])

            return redirect('contact_success')  # Redirect after success
    else:
        form = ContactForm()
    
    context = {
        'compositions': compositions,
        'genres_dict': genres_dict,
        'services': services,
        'form':form,
    }
    
    return render(request, 'musicshowcase/index.html', context)




