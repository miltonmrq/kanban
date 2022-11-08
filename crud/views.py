
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Tarea, Tablero

# Create your views here.


class ListarTareaView(ListView):
    model = Tarea
    template_name = 'home.html'


class ListarTableroView(ListView):
    model = Tablero
    template_name = "home.html"


class CrearTarea(CreateView):
    model = Tarea
    fields = ["tablero", "titulo", "descripcion", "creado", "due_date",]
