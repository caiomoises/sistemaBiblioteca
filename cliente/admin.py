from django.contrib import admin
from .models import *

@admin.register(cliente)
class clienteAdmin(admin.ModelAdmin):
    list_display = 'Nome', 'CPF', 'Contato'
    list_filter = ('Nome', 'CPF')

    