import imp
import re
from django.http import HttpResponse
from django.shortcuts import render
from GimCoder.models import *
from GimCoder.forms import *

# Create your views here.

def clientes(request):
     try:
          data = request.GET['nombre']
          print (data)
          if data:
               cliente1 = cliente.objects.filter( nombre = data )
               print (cliente1)
               return render(request,"GimCoder/clientes.html", {"cliente": cliente1[0]})
     except:
          return render(request,"GimCoder/clientes.html")


def profesores(request):
     try:
          data = request.GET['nombre']
          print (data)
          if data:
               ejercicio1 = profesor.objects.filter( nombre = data )
               print (profesor1)
               return render(request,"GimCoder/profesores.html", {"profesor": profesor1[0]})
     except:
          return render(request,"GimCoder/profesores.html")

def rutinas(request):

     return render(request,"GimCoder/rutinas.html")

def ejercicios(request):
     try:
          data = request.GET['nombre']
          print (data)
          if data:
               ejercicio1 = ejercicio.objects.filter( nombre = data )
               print (ejercicio1)
               return render(request,"GimCoder/ejercicios.html", {"ejercicio": ejercicio1[0]})
     except:
          return render(request,"GimCoder/ejercicios.html")

def formularioclientes(request):
     if request.method == "POST":
          nuevocliente = clienteform(request.POST)
          
          if nuevocliente.is_valid():
               print("Formulario Valido")
               data = nuevocliente.cleaned_data
               carganuevocliente = cliente(nombre = data['nombre'], apellido = data['apellido'], email = data['email'] , peso = data['peso'], altura = data['altura'])
               carganuevocliente.save()     

          return render(request,"GimCoder/clientes.html")
     
     else:
          
          formulario = clienteform()
          
          return render(request,"GimCoder/formularioclientes.html", {"formulario": formulario})

def formularioprofes(request):
     if request.method == "POST":
          nuevoprofesor = profesorform(request.POST)
          
          if nuevoprofesor.is_valid():
               print("Formulario Valido")
               data = nuevoprofesor.cleaned_data
               carganuevoprofesor = profesor(nombre = data['nombre'], apellido = data['apellido'], turno = data['turno'])
               carganuevoprofesor.save()

          return render(request,"GimCoder/clientes.html")
     
     else:
          
          formulario = profesorform()
          
          return render(request,"GimCoder/formularioprofesores.html", {"formulario": formulario})

def formularioejercicios(request):
     if request.method == "POST":
          nuevoejercicio = ejercicioform(request.POST)
          
          if nuevoejercicio.is_valid():
               print("Formulario Valido")
               data = nuevoejercicio.cleaned_data
               carganuevoejercicio = ejercicio(nombre = data['nombre'], detalle = data['detalle'], demostracion = data['demostracion'], repeticiones = data['repeticiones'], duracion = data['duracion'])
               carganuevoejercicio.save()

          return render(request,"GimCoder/ejercicios.html")
     
     else:
          
          formulario = ejercicioform()
          
          return render(request,"GimCoder/formularioejercicios.html", {"formulario": formulario})



def inicio(request):
    nombre_gim= "Dara's 4 Gimnasia"
    lema = "Solo del esfuerzo personal se obtiene los logros"
    dict_index = {"nombre_gim": nombre_gim, "lema": lema}
    return render(request,"GimCoder/index.html", dict_index)