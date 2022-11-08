from django import forms


from .models import Tablero, Tarea


class TableroForm(forms.ModelForm):
    model = Tablero
    fields = {'titulo',}
    

