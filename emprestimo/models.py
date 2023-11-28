from django.db import models
from livro.models import livro
from cliente.models import cliente
from datetime import datetime, timedelta

def livros_emprestado():
    emprestimos_ativos = emprestimo.objects.filter(devolucao__gte=datetime.now().date())

    livros_emprestados = [emprestimo.livro_emprestado for emprestimo in emprestimos_ativos]

    return livros_emprestados

class emprestimo(models.Model):
    livro_emprestado = models.ForeignKey(livro, on_delete=models.CASCADE)
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    devolucao = models.DateField(default=datetime.now().date() + timedelta(days=15))

    def __str__(self) -> str:
        return f"{self.livro_emprestado.nome} - Emprestado para: {self.cliente.nome}"