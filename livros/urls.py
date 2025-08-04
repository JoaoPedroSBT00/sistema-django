from django.urls import path
from . import views

urlpatterns = [
    path('criar_livro/', views.criar_livro, name='criar_livro'),
    path('', views.home, name='home')
]