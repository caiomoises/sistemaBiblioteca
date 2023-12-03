from django.db import models
from livro.models import livro
from cliente.models import cliente
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError

class emprestimo(models.Model):
    livro_emprestado = models.ForeignKey(livro, on_delete=models.CASCADE)
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(default=datetime.now().date(), editable=False)
    devolucao = models.DateField(default=datetime.now().date() + timedelta(days=15), editable=False)

    def __str__(self) -> str:
        return f"{self.livro_emprestado.nome} - Emprestado para: {self.cliente.nome}"

    def clean(self):
        # Verificar se o cliente já possui um empréstimo ativo
        emprestimos_ativos = emprestimo.objects.filter(cliente=self.cliente, devolucao__gte=datetime.now().date())
        
        if emprestimos_ativos.exists():
            raise ValidationError('Este cliente já possui um livro emprestado.')

    def save(self, *args, **kwargs):
        # Chamar o clean() automaticamente antes de salvar
        self.clean()
        super().save(*args, **kwargs)
