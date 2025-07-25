from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("livros/", include("livros.urls")),
    path('admin/', admin.site.urls),
]
