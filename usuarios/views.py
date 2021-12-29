from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    '''Cadastra um novo usuário.'''
    if request.method != 'POST':
        # Exibe um formulário em branco
        form = UserCreationForm()
    else:
        # Processa o formulário preenchido
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Faz login do usuário e o redireciona para a página principal
            login(request, new_user)
            return redirect('escalas:index')
    # Exibe um formulário em branco ou inválido
    context = {'form': form}
    return render(request, 'registration/register.html', context)
    



