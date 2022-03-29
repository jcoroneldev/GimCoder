import imp
from django.contrib import admin
from GimCoder.models import cliente, profesor, rutina, ejercicio 

admin.site.register(cliente)
admin.site.register(profesor)
admin.site.register(rutina)
admin.site.register(ejercicio)