from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.composition_list, name='composition_list'),
    path('components/', views.components, name='components'),
    path('index/', views.index, name='index'),
    path('contact-success/', TemplateView.as_view(template_name='contact_success.html'), name='contact_success'),

]
