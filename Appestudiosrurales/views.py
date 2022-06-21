from django.shortcuts import render
from django.http import HttpResponse
from Appestudiosrurales.models import Category, post, Comentarios, Investigadorxs, Publicaciones, Actividades_eventos, sobre_mi


def categorias (self):
    categorias = Category (name = 'género_y_ruralidad')
    categorias.save()
    documento = f"Category: {categorias.name}"
    return HttpResponse (documento)
# Create your views here.





