from django.db import models

class livro(models.Model):
    idiomas = [
        ('pt', 'Português'),
        ('en', 'Inglês'),
        ('es', 'Espanhol'),
        ('fr', 'Francês'),
        ('de', 'Alemão'),
        ('it', 'Italiano'),
        ('ja', 'Japonês'),
        ('zh', 'Chinês (Mandarim)'),
        ('ko', 'Coreano'),
        ('ru', 'Russo'),
        ('ar', 'Árabe'),
        ('hi', 'Hindi'),
        ('sw', 'Suaíli'),
        ('tr', 'Turco'),
        ('nl', 'Holandês'),
    ]

    ano_publica = [(ano, str(ano)) for ano in range(1500, 2024)]

    nome = models.CharField(max_length=50, blank=False)
    editora = models.CharField(max_length=50, blank=False, default='')
    idioma = models.CharField(max_length=2, choices=idiomas, default='pt')
    codigo = models.CharField(max_length=50, blank=False, default='')
    publicacao = models.IntegerField(choices=ano_publica, default='2023') 
    edicao = models.CharField(max_length=5, blank=False, default='')
    quantidade = models.IntegerField(blank=False) 

    def __str__(self) -> str:
        return self.nome