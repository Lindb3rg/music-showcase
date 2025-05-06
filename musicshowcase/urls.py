from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'musicshowcase'


urlpatterns = [
    path('', views.index, name='index'),  # This will be accessible at /
    path('success/', TemplateView.as_view(template_name='musicshowcase/contact_success.html'), name='contact_success'),  # Accessible at /success/
    path('user_login/', views.user_login, name='user_login'),
    path('logout/', views.logout_user, name='logout'),  # Accessible at /logout/
]



