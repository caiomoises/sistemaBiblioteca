from django.contrib import admin
from .models import *

@admin.register(livro)
class livroAdmin(admin.ModelAdmin):
    list_display = ('Nome', 'Idioma', 'Codigo', 'Edição', 'Quantidade')
    search_fields = 'Nome', 'Codigo'
    list_per_page = 10
