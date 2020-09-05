from django.urls import reverse_lazy
from .models import Estudiante
from .form import Estudianteform
from django.views.generic import ListView,CreateView,DeleteView,UpdateView


# relaciona la parte vista con el template home.html

class lista_estudiante(ListView):
    model = Estudiante
    template_name = 'consulta_estudiante.html'

class crear_estudiante(CreateView):
    model = Estudiante
    form_class = Estudianteform
    template_name = 'formulario_estudiante.html'
    success_url = reverse_lazy('home')

class update_estudiante(UpdateView):
    model = Estudiante
    form_class = Estudianteform
    template_name = 'formulario_estudiante.html'
    success_url = reverse_lazy('consulta_estudiante')

class delete_estudiante(DeleteView):
    model = Estudiante
    template_name = 'verificar_estudiante.html'
    success_url = reverse_lazy('consulta_estudiante')

