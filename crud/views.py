
from django.views.generic import ListView, DetailView 
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Tablero

# Create your views here.



class ListarTareas(ListView):
    model = Tablero
    template_name = 'home.html'
