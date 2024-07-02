from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Evento, Inscripcion
from .forms import EventoForm

@login_required
def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.creador = request.user
            evento.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm()
    return render(request, 'eventos/crear_evento.html', {'form': form})

@login_required
def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})

@login_required
def inscribirse_evento(request, evento_id):
    evento = Evento.objects.get(id=evento_id)
    Inscripcion.objects.create(evento=evento, usuario=request.user)
    return JsonResponse({'message': 'Inscripción exitosa!'})

@login_required
def detalle_evento(request, evento_id):
    evento = Evento.objects.get(id=evento_id)
    inscripciones = Inscripcion.objects.filter(evento=evento)
    return render(request, 'eventos/detalle_evento.html', {'evento': evento, 'inscripciones': inscripciones})


from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


