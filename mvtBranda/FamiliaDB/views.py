from django.shortcuts import render, HttpResponse
from FamiliaDB.models import *
# Create your views here.

def index(request):
    
    parentezco = [x.parentezco for x in Familiar.objects.all()]
    nombre = [x.nombre for x in Familiar.objects.all()]
    edad = [x.edad for x in Familiar.objects.all()]
    nacimiento = [x.nacimiento for x in Familiar.objects.all()]
    
    especie = [x.especie for x in Mascota.objects.all()]
    nombre_mascota = [x.nombre for x in Mascota.objects.all()]
    
    return render(request, 'FamiliaDB/index.html', {"parentezco": parentezco, "nombre": nombre, "edad": edad, "nacimiento": nacimiento, "especie":especie, "nombre_mascota":nombre_mascota})
   