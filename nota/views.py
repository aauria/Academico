from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Notas
from .form import NotaForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
# Create your views here.

class lista_notas(PermissionRequiredMixin,ListView):
    model = Notas
    template_name = 'nota/consulta_nota.html'
    permission_required = 'nota.view_notas'

class crear_notas(PermissionRequiredMixin,CreateView):
    model = Notas
    form_class = NotaForm
    template_name = 'nota/formulario_nota.html'
    success_url = reverse_lazy('consulta_nota')
    permission_required = 'nota.add_notas'

class update_notas(PermissionRequiredMixin,UpdateView):
    model = Notas
    form_class = NotaForm
    template_name = 'nota/formulario_nota.html'
    success_url = reverse_lazy('consulta_nota')
    permission_required = 'nota.change_notas'

class delete_notas(PermissionRequiredMixin,DeleteView):
    model = Notas
    template_name = 'nota/verificar_nota.html'
    success_url = reverse_lazy('consulta_nota')
    permission_required = 'nota.delete_notas'