from django import forms

   
class profesorform(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    turno = forms.CharField(max_length=40)

class clienteform(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    peso = forms.IntegerField()
    altura = forms.IntegerField()

class rutinaform(forms.Form):
    repeticiones = forms.IntegerField()
    ejercicio1 = forms.CharField(max_length=40)
    ejercicio2 = forms.CharField(max_length=40)
    ejercicio3 = forms.CharField(max_length=40)
    ejercicio4 = forms.CharField(max_length=40)
    ejercicio5 = forms.CharField(max_length=40)
    ejercicio6 = forms.CharField(max_length=40)

class ejercicioform(forms.Form):
    nombre = forms.CharField(max_length=40)
    detalle = forms.CharField(max_length=80)
    demostracion = forms.CharField(max_length=40)
    repeticiones = forms.IntegerField()
    duracion = forms.TimeField()
    
