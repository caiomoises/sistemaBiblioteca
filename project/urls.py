from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cliente.urls')),
    path('', include('livro.urls')),
    path('', include('emprestimo.urls')),   
]
