'''Define padrões de URL para usuarios'''

from django.urls import path, include

app_name = 'usuarios'
urlpatterns = [
    # Página de login
    path('', include('django.contrib.auth.urls')),

]