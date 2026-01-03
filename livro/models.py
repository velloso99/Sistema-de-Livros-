from django.db import models
from datetime import date

class Livros(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=30)
    co_autor = models.CharField(max_length=30, blank=True)
    data_cadastro = models.DateField( default=date.today)
    emprestado = models.BooleanField(default=False)
    nome_emprestimo = models.CharField(max_length=30, blank=True)
    data_emprestimo = models.DateTimeField(blank=True)
    data_devolucao = models.DateTimeField(blank=True)
    tempo_emprestimo = models.DateTimeField(blank=True)

    class Meta:
        verbose_name = "Livro"

