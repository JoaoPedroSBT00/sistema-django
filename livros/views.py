from django.shortcuts import render, redirect
from .models import livros
from .forms import livroForm

def livro(request):
    livro = livros.objects.all() .order_by('titulo')
    return render(request, 'livros/livro.html', {'livro': livro})

def criar_livro(request):
    if request.method == 'POST':
        form = livroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livro')
    else:
        form = livroForm()
    return render(request, 'livros/criar_livro.html', {'form': form})

def remover(request, id_livro):
    livro = livros.objects.get(id=id_livro)
    if request.method == 'GET':
        livro.delete()
        return redirect('livro')
    return render(request, 'livros/remover.html', {'livro': livro})

def editar(request, id_livro):
    livro_obj = livros.objects.get(id=id_livro)
    if request.method == 'POST':
        form = livroForm(request.POST, instance=livro_obj)
        if form.is_valid():
            form.save()
            return redirect('livro')
    else:
        form = livroForm(instance=livro_obj)
    return render(request, 'livros/editar.html', {'form': form, 'livro': livro_obj})


def detalhe(request, id_livro):
    livro = livros.objects.get(id=id_livro)

    return render(request, 'livros/detalhe.html', {'livro': livro})

    
def home(request):
    if request.method == 'GET':
        return render(request, 'livros/index.html')