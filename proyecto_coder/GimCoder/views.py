import imp
import re
from django.http import HttpResponse
from django.shortcuts import render
from GimCoder.models import *
from GimCoder.forms import ClienteFormulario

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
          NuevoClienteFormulario = ClienteFormulario(request.POST)
          print (NuevoClienteFormulario)
          if NuevoClienteFormulario.is_valid:
               cliente1 = NuevoClienteFormulario.cleaned_data
               clientenuevo = cliente(cliente1['nombre'],cliente1['apellido'],cliente1['email'])
               clientenuevo.save()
          return render(request,"clientes.html")
     else:
          
          NuevoClienteFormulario = ClienteFormulario()
          
          return render(request,"GimCoder/formularioclientes.html", {"Formulario": NuevoClienteFormulario})

def inicio(request):
    nombre_gim= "Dara's 4 Gimnasia"
    lema = "Solo del esfuerzo personal se obtiene los logros"
    dict_index = {"nombre_gim": nombre_gim, "lema": lema}
    return render(request,"GimCoder/index.html", dict_index)