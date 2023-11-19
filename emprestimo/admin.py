from django.contrib import admin
from .models import *
from livro.models import *

@admin.register(emprestimo) 
class emprestimoAdmin(admin.ModelAdmin):
    list_display = ('livro_emprestado', 'cliente',)
    # search_fields = 'cliente',