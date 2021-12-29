from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Plantao
from .forms import PlantaoForm


def index(request):
    '''A página inicial de escalas.'''
    return render(request, 'escalas/index.html')


@login_required
def plantoes(request):
    '''Mostra todos os plantões.'''
    plantoes = Plantao.objects.order_by('data_plantao')
    context = {'plantoes': plantoes}
    return render(request, 'escalas/plantoes.html', context)


@login_required
def novo_plantao(request):
    '''Adiciona um novo plantão.'''
    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulário em branco
        form = PlantaoForm()
    else:
        # Dados de POST submetidos; processa os dados
        form = PlantaoForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('escalas:plantoes')

    # Exibe um formulário em branco ou inválido
    context = {'form': form}
    return render(request, 'escalas/novo_plantao.html', context)
