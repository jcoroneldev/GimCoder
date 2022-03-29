import re
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def clientes(request):

    return render(request,"GimCoder/clientes.html")

def profesores(request):

     return render(request,"GimCoder/profesores.html")

def rutinas(request):

     return render(request,"GimCoder/rutinas.html")

def ejercicios(request):

     return render(request,"GimCoder/ejercicios.html")

def inicio(request):
    nombre_gim= "Dara's 4 Gimnasia"
    lema = "Solo del esfuerzo personal se obtiene los logros"
    dict_index = {"nombre_gim": nombre_gim, "lema": lema}
    return render(request,"GimCoder/index.html", dict_index)