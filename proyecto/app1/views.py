from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Carrera

def listar_carrera(request):
    #obtega todas las carras 
    carreras = Carrera.objects.all()
    #indico a que vista html enviar estas carreras
    return render(request, 'carrera.html', {'saludo':'es una prueba', 'carreras':carreras} ) 

