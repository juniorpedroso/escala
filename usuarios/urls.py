'''Define padrões de URL para usuarios'''

from django.urls import path, include
from . import views

app_name = 'usuarios'
urlpatterns = [
    # Página de login
    path('', include('django.contrib.auth.urls')),

    # Página de cadastro
    path('register/', views.register, name='register'),

]