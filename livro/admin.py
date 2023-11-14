from django.contrib import admin
from .models import *

@admin.register(livro)
class livroAdmin(admin.ModelAdmin):
    list_display = ('Nome',)