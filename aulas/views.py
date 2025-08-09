from django.shortcuts import render, redirect
from .models import Aula
from .forms import AulaForm


def index(request):
    
    aulas = Aula.objects.all().order_by('conteudo')
    return render(request, 'aulas/index.html', {'aulas': aulas})

def add(request):
    if request.method == 'POST':
        form = AulaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aulas_index')
    else:
        form = AulaForm()
    return render(request, 'aulas/adicionar.html', {'form': form})

def edit(request, id_aula):
    aulas = Aula.objects.get(id=id_aula)
    if request.method == 'POST':
        form = AulaForm(request.POST, instance=aulas)
        if form.is_valid():
            form.save()
            return redirect('aulas/index.html')
    else:
        form = AulaForm(instance=aulas)
    return render(request, 'aulas/editar.html', {'form': form, 'aulas': aulas})

def delete(request, id_aula):
    aulas = Aula.objects.get(id=id_aula)
    if request.method == 'GET':
        aulas.delete()
        return redirect('aulas/index.html')
    return render(request, 'aulas/remover.html', {'aulas': aulas})

def detalhe(request, id_aula):
    Aulas = Aula.objects.get(id=id_aula)

    return render(request, 'aulas/detalhe.html', {'aulas': aulas})


