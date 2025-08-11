from django import forms
from .models import livros


class livroForm(forms.ModelForm):
    class Meta:
        model = livros
        fields = ['titulo', 'autor', 'editora', 'ano']