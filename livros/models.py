from django.db import models

class livros(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    ano = models.IntegerField()

def __str__(self):
    return self.titulo