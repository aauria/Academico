from django.urls import reverse_lazy
from .models import Materia
from .form import Materiaform
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
# Create your views here.

class lista_materia(ListView):
    model = Materia
    template_name = 'consulta_materia.html'

class crear_materia(CreateView):
    model = Materia
    form_class = Materiaform
    template_name = 'formulario_materia.html'
    success_url = reverse_lazy('home')

class update_materia(UpdateView):
    model = Materia
    form_class = Materiaform
    template_name = 'formulario_materia.html'
    success_url = reverse_lazy('consulta_materia')

class delete_materia(DeleteView):
    model = Materia
    template_name = 'verificar_materia.html'
    success_url = reverse_lazy('consulta_materia')

# Create your views here.
