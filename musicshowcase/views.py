from django.shortcuts import render,redirect
from .models import Composition, Service, Image
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
import boto3
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required






def index(request):
    
    compositions = Composition.objects.all()
    services = Service.objects.all()
    images = Image.objects.all()
    
    unique_genres = Composition.objects.values_list('genre', flat=True).distinct()
    genres_dict = {genre: genre.replace('_', ' ') for genre in unique_genres}
    
    
    success = False
    
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_message = f"Message from {name} ({email}):\n\n{message}"

            
            send_mail(subject, full_message, email, [settings.DEFAULT_FROM_EMAIL])
            
            success = True
            
            return redirect('musicshowcase:contact_success')    

    else:
        form = ContactForm()
    
    context = {
        'compositions': compositions,
        'genres_dict': genres_dict,
        'services': services,
        'form':form,
        'success':success,
        'images':images,

    }
    
    return render(request, 'musicshowcase/index.html', context)




def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('musicshowcase:index'))  
            else:
                return HttpResponse("Account not active")
        else:
            print(f"Someone tried to login and failed. Username: {username} and password: {password}")
            return render(request, 'musicshowcase/login.html', {'error': 'Invalid credentials.'})
    else:
        return render(request, 'musicshowcase/login.html')
    

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('musicshowcase:index')
        else:
            # Handle login failure
            return render(request, 'musicshowcase/login.html', {'error': 'Invalid credentials.'})
    else:
        return render(request, 'musicshowcase/login.html')    
    


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('musicshowcase:user_login')) 
