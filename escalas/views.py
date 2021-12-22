from django.shortcuts import render

from .models import Plantao

# Create your views here.

def index(request):
    '''A página inicial de escalas.'''
    return render(request, 'escalas/index.html')


def plantoes(request):
    '''Mostra todos os plantões.'''
    plantoes = Plantao.objects.order_by('data_plantao')
    context = {'plantoes': plantoes}
    return render(request, 'escalas/plantoes.html', context)