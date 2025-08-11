from django.urls import path
from . import views

urlpatterns = [
    path('livros/', views.livro, name='livro'),
    path('criar_livro/', views.criar_livro, name='criar_livro'),
    path('<int:id_livro>/', views.detalhe, name='detalhe'),
    path('remover/<int:id_livro>/', views.remover, name='remover'),
    path('editar/<int:id_livro>/', views.editar, name='editar'),
]
