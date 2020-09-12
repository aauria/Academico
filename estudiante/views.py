from django.urls import reverse_lazy
from .models import Estudiante,EstudianteMateriaDocente,EstudianteMateriaCurso
from .form import Estudianteform,EstudianteMateriaDocenteform,EstudianteMateriaCursoform
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

class lista_estudiantemateriacurso(ListView):
    model = EstudianteMateriaCurso
    template_name = 'consulta_estudiantemateriacurso.html'

class crear_estudiantemateriacurso(CreateView):
    model = EstudianteMateriaCurso
    form_class = EstudianteMateriaCursoform
    template_name = 'formulario_estudiantemateriacurso.html'
    success_url = reverse_lazy('home')

class update_estudiantemateriacurso(UpdateView):
    model = EstudianteMateriaCurso
    form_class = EstudianteMateriaCursoform
    template_name = 'formulario_estudiantemateriacurso.html'
    success_url = reverse_lazy('consulta_estudiante_mat_curso')

class delete_estudiantemateriacurso(DeleteView):
    model = EstudianteMateriaCurso
    template_name = 'verificar_estudiantemateriacurso.html'
    success_url = reverse_lazy('consulta_estudiante_mat_curso')
