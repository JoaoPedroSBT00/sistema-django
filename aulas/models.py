from django.db import models

class Aula(models.Model):
    conteudo = models.TextField()
    duracao = models.IntegerField()


    def __str__(self):
        return self.conteudo
    
