import imp
from django.urls import path
from GimCoder.views import *

urlpatterns = [
    path('inicio/', inicio, name="inicio"),
    path('profesores/', profesores, name="profesores"),
    path('clientes/', clientes, name="clientes"),
    path('rutinas/', rutinas, name="rutinas"),
    path('ejercicios/', ejercicios, name="ejercicios"),

]
