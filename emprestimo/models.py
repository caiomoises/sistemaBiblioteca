from django.db import models
from livro.models import livro
from cliente.models import cliente
from datetime import datetime, timedelta

class emprestimo(models.Model):
    livro_emprestado = models.ForeignKey(livro, on_delete=models.CASCADE)
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    devolução = models.DateField(default=datetime.now().date() + timedelta(days=15))

    def __str__(self) -> str:
        return f"{self.livro_emprestado.Nome} - Emprestado para: {self.cliente.Nome}"