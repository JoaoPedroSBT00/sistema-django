from django.shortcuts import render, redirect
from .models import Materia
from .forms import MateriaForm


def index(request):

    Materia = Materia.objects.all() .order_by('nome')
    return render(request, 'materia/index.html', {'materia': materias})

def add(request):
    if request.method == 'POST':
        form = MateriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MateriaForm()
    return render(request, 'materia/adicionar.html', {'form': form})

def edit(request, id_materia):
    materia = Materia.objects.get(id=id_materia)
    if request.method == 'POST':
        form = MateriaForm(request.POST, instance=materia)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MateriaForm(instance=materia)
    return render(request, 'materia/editar.html', {'form': form, 'materia': materia})

def delete(request, id_materia):
    materia = Materia.objects.get(id=id_materia)
    if request.method == 'POST':
        Materia.delete()
        return redirect('index')
    return render(request, 'materias/remover.html', {'materia': materia})


