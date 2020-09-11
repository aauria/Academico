from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Notas
from .form import NotaForm
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
# Create your views here.

class lista_notas(ListView):
    model = Notas
    template_name = 'consulta_notas.html'

class crear_notas(CreateView):
    model = Notas
    form_class = NotaForm
    template_name = 'formulario_nota.html'
    success_url = reverse_lazy('home')

class update_notas(UpdateView):
    model = Notas
    form_class = NotaForm
    template_name = 'formulario_nota.html'
    success_url = reverse_lazy('consulta_nota')

class delete_notas(DeleteView):
    model = Notas
    template_name = 'verificar_nota.html'
    success_url = reverse_lazy('consulta_nota')