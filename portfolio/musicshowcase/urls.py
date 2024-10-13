from django.urls import path
from . import views

urlpatterns = [
    path('', views.composition_list, name='composition_list'),
    path('components/', views.components, name='components'),
    path('index/', views.index, name='index'),
]
