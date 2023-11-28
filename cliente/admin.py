from django.contrib import admin
from .models import *

@admin.register(cliente)
class clienteAdmin(admin.ModelAdmin):
    list_display = 'nome', 'cpf', 'contato', 
    list_filter = ('nome', 'cpf')
    search_fields = 'nome', 'cpf', 'contato'

    