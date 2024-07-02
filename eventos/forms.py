from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'descripcion', 'ubicacion', 'fecha_hora']
