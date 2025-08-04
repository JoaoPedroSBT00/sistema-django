from django.shortcuts import render

def criar_livro(request):
    if request.method == 'GET':
        return render(request, 'livros/criar_livro.html')
    
def home(request):
    if request.method == 'GET':
        return render(request, 'livros/index.html')