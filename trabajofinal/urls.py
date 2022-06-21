

from django.contrib import admin
from django.urls import path
from Appestudiosrurales.views import categorias
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path ('categorias/', categorias),
]
