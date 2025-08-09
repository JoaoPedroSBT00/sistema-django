from django.shortcuts import render, redirect
from .models import Materia
from .forms import MateriaForm


def index(request):

    materias = Materia.objects.all() .order_by('nome')
    return render(request, 'materias/index.html', {'materias': materias})

def add(request):
    if request.method == 'POST':
        form = MateriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MateriaForm()
    return render(request, 'materias/adicionar.html', {'form': form})

def edit(request, id_materia):
    materias = Materia.objects.get(id=id_materia)
    if request.method == 'POST':
        form = MateriaForm(request.POST, instance=materias)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MateriaForm(instance=materias)
    return render(request, 'materias/editar.html', {'form': form, 'materias': materias})

def delete(request, id_materia):
    materias = Materia.objects.get(id=id_materia)
    if request.method == 'GET':
        materias.delete()
        return redirect('index')
    return render(request, 'materias/remover.html', {'materias': materias})

def detalhe(request, id_materia):
    materias = Materia.objects.get(id=id_materia)

    return render(request, 'materias/detalhe.html', {'materias': materias})


