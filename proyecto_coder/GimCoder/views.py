import imp
import re
from django.http import HttpResponse
from django.shortcuts import render
from GimCoder.models import *
from GimCoder.forms import *

# Create your views here.

def clientes(request):

    return render(request,"GimCoder/clientes.html")

def profesores(request):

     return render(request,"GimCoder/profesores.html")

def rutinas(request):

     return render(request,"GimCoder/rutinas.html")

def ejercicios(request):

     return render(request,"GimCoder/ejercicios.html")

def formularioclientes(request):
     if request.method == "POST":
          nuevocliente = clienteform(request.POST)
          
          if nuevocliente.is_valid:
               print("Formulario Valido")
               nuevoclientelimpio = nuevocliente.cleaned_data

          return render(request,"GimCoder/clientes.html")
     
     else:
          
          formulario = clienteform()
          
          return render(request,"GimCoder/formularioprofesores.html", {"formulario": formulario})

def formularioprofes(request):
     if request.method == "POST":
          nuevoprofesor = profesorform(request.POST)
          
          if nuevoprofesor.is_valid:
               print("Formulario Valido")
               nuevoprofesorlimpio = nuevoprofesor.cleaned_data

          return render(request,"GimCoder/clientes.html")
     
     else:
          
          formulario = profesorform()
          
          return render(request,"GimCoder/formularioprofesores.html", {"formulario": formulario})

def inicio(request):
    nombre_gim= "Dara's 4 Gimnasia"
    lema = "Solo del esfuerzo personal se obtiene los logros"
    dict_index = {"nombre_gim": nombre_gim, "lema": lema}
    return render(request,"GimCoder/index.html", dict_index)