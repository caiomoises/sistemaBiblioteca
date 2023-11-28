from django.contrib import admin
from .models import *

@admin.register(livro)
class livroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idioma', 'codigo', 'edicao', 'quantidade')
    search_fields = 'nome', 'codigo'
    list_per_page = 10
