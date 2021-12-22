'''Define padrões de URL para escalas.'''

from django.urls import path

from . import views

app_name = 'escalas'
urlpatterns = [
    # Página inicial
    path('', views.index, name='index'),

    # Mostra todos os assuntos
    path('plantoes/', views.plantoes, name='plantoes'),
]