from django.urls import reverse_lazy
from .models import Materia
from .form import Materiaform
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
# Create your views here.

class lista_materia(PermissionRequiredMixin,ListView):
    model = Materia
    template_name = 'materia/consulta_materia.html'
    permission_required = 'materia.view_materia'

class crear_materia(PermissionRequiredMixin,CreateView):
    model = Materia
    form_class = Materiaform
    template_name = 'materia/formulario_materia.html'
    success_url = reverse_lazy('consulta_materia')
    permission_required = 'materia.add_materia'

class update_materia(PermissionRequiredMixin,UpdateView):
    model = Materia
    form_class = Materiaform
    template_name = 'materia/formulario_materia.html'
    success_url = reverse_lazy('consulta_materia')
    permission_required = 'materia.change_materia'

class delete_materia(PermissionRequiredMixin,DeleteView):
    model = Materia
    template_name = 'materia/verificar_materia.html'
    success_url = reverse_lazy('consulta_materia')
    permission_required = 'materia.delete_materia'


# Create your views here.
