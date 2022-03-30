from django import forms

class  ClienteFormulario(forms.Form):
    Nombre: forms.CharField()
    Apellido: forms.CharField()
    Email: forms.EmailField()
    Peso: forms.IntegerField()
    Altura: forms.IntegerField()
