from django.contrib import admin
from django.urls import include, path
from materias import views as materias_views
from livros import views as livros_views
from aulas import views as aulas_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', livros_views.home, name='home'),
    #livros
    path("livros/", include("livros.urls")),
    #materias
    path('materias/', materias_views.index, name='index'),
    path('materias/adicionar/', materias_views.add, name='add'),
    path('materias/editar/<int:id_materia>/', materias_views.edit, name='edit'),
    path('materias/remover/<int:id_materia>/', materias_views.delete, name='delete'),
    path('materias/<int:id_materia>/', materias_views.detalhe, name='detail'),
    #aulas
    path('aulas/', aulas_views.index, name='aulas_index'),
    path('aulas/adicionar/', aulas_views.add, name='aulas_add'),
    path('aulas/editar/<int:id_aula>/', aulas_views.edit, name='aulas_edit'),
    path('aulas/remover/<int:id_aula>/', aulas_views.delete, name='aulas_delete'),
    path('aulas/<int:id_aula>/', aulas_views.detalhe, name='aulas_detail'),
]
