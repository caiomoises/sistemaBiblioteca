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

    Nome = models.CharField(max_length=150, blank=False)
    Editora = models.CharField(max_length=50, blank=False, default='')
    Idioma = models.CharField(max_length=2, choices=idiomas, default='pt')
    Codigo = models.CharField(max_length=50, blank=False, default='')
    Publicação = models.IntegerField(choices=ano_publica, default='2023') 
    Edição = models.CharField(max_length=5, blank=False, default='')
    Quantidade = models.IntegerField(blank=False) 

    def __str__(self) -> str:
        return self.Nome