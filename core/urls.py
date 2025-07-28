from django.contrib import admin
from django.urls import include, path
from materias import views as materias_views

urlpatterns = [
    path("livros/", include("livros.urls")),
    path('admin/', admin.site.urls),
    #materias
    path('materia/', materias_views.index, name='index'),
    path('materias/adicionar/', materias_views.add, name='add'),
    path('materias/editar/<int:id_materia>/', materias_views.edit, name='edit'),
    path('materias/deletar/<int:id_materia>/', materias_views.delete, name='delete'),
    
]
