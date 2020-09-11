from django.urls import reverse_lazy
from .models import Estudiante,EstudianteMateriaDocente
from .form import Estudianteform,EstudianteMateriaDocenteform
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



class lista_estudiantedocentemateria(ListView):
    model = EstudianteMateriaDocente
    template_name = 'consulta_estudiantedocentemateria.html'

class crear_estudiantedocentemateria(CreateView):
    model = EstudianteMateriaDocente
    form_class = EstudianteMateriaDocenteform
    template_name = 'formulario_estudiantedocentemateria.html'
    success_url = reverse_lazy('home')

class update_estudiantedocentemateria(UpdateView):
    model = EstudianteMateriaDocente
    form_class = EstudianteMateriaDocenteform
    template_name = 'formulario_estudiantedocentemateria.html'
    success_url = reverse_lazy('consulta_estudiante_doc_mat')

class delete_estudiantedocentemateria(DeleteView):
    model = EstudianteMateriaDocente
    template_name = 'verificar_estudiantedocentemateria.html'
    success_url = reverse_lazy('consulta_estudiante_doc_mat')

