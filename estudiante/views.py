from django.urls import reverse_lazy
from .models import Estudiante,EstudianteMateriaDocente,EstudianteMateriaCurso
from .form import Estudianteform,EstudianteMateriaDocenteform,EstudianteMateriaCursoform
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin


# relaciona la parte vista con el template home.html

class lista_estudiante(PermissionRequiredMixin,ListView):
    model = Estudiante
    template_name = 'estudiante/consulta_estudiante.html'
    permission_required = 'estudiante.view_estudiante'

class crear_estudiante(PermissionRequiredMixin,CreateView):
    model = Estudiante
    form_class = Estudianteform
    template_name = 'estudiante/formulario_estudiante.html'
    success_url = reverse_lazy('consulta_estudiante')
    permission_required = 'estudiante.add_estudiante'

class update_estudiante(PermissionRequiredMixin,UpdateView):
    model = Estudiante
    form_class = Estudianteform
    template_name = 'estudiante/formulario_estudiante.html'
    success_url = reverse_lazy('consulta_estudiante')
    permission_required = 'estudiante.change_estudiante'

class delete_estudiante(PermissionRequiredMixin,DeleteView):
    model = Estudiante
    template_name = 'estudiante/verificar_estudiante.html'
    success_url = reverse_lazy('consulta_estudiante')
    permission_required = 'estudiante.delete_estudiante'



class lista_estudiantedocentemateria(PermissionRequiredMixin,ListView):
    model = EstudianteMateriaDocente
    template_name = 'estudiante/consulta_estudiantedocentemateria.html'
    permission_required = 'estudiante.view_estudiantemateriadocente'

class crear_estudiantedocentemateria(PermissionRequiredMixin,CreateView):
    model = EstudianteMateriaDocente
    form_class = EstudianteMateriaDocenteform
    template_name = 'estudiante/formulario_estudiantedocentemateria.html'
    success_url = reverse_lazy('consulta_estudiante_doc_mat')
    permission_required = 'estudiante.add_estudiantemateriadocente'

class update_estudiantedocentemateria(PermissionRequiredMixin,UpdateView):
    model = EstudianteMateriaDocente
    form_class = EstudianteMateriaDocenteform
    template_name = 'estudiante/formulario_estudiantedocentemateria.html'
    success_url = reverse_lazy('consulta_estudiante_doc_mat')
    permission_required = 'estudiante.change_estudiantemateriadocente'


class delete_estudiantedocentemateria(PermissionRequiredMixin,DeleteView):
    model = EstudianteMateriaDocente
    template_name = 'estudiante/verificar_estudiantedocentemateria.html'
    success_url = reverse_lazy('consulta_estudiante_doc_mat')
    permission_required = 'estudiante.delete_estudiantemateriadocente'

class lista_estudiantemateriacurso(PermissionRequiredMixin,ListView):
    model = EstudianteMateriaCurso
    template_name = 'estudiante/consulta_estudiantemateriacurso.html'
    permission_required = 'estudiante.view_estudiantemateriacurso'

class crear_estudiantemateriacurso(PermissionRequiredMixin,CreateView):
    model = EstudianteMateriaCurso
    form_class = EstudianteMateriaCursoform
    template_name = 'estudiante/formulario_estudiantemateriacurso.html'
    success_url = reverse_lazy('consulta_estudiante_mat_curso')
    permission_required = 'estudiante.add_estudiantemateriacurso'


class update_estudiantemateriacurso(PermissionRequiredMixin,UpdateView):
    model = EstudianteMateriaCurso
    form_class = EstudianteMateriaCursoform
    template_name = 'estudiante/formulario_estudiantemateriacurso.html'
    success_url = reverse_lazy('consulta_estudiante_mat_curso')
    permission_required = 'estudiante.change_estudiantemateriacurso'

class delete_estudiantemateriacurso(PermissionRequiredMixin,DeleteView):
    model = EstudianteMateriaCurso
    template_name = 'estudiante/verificar_estudiantemateriacurso.html'
    success_url = reverse_lazy('consulta_estudiante_mat_curso')
    permission_required = 'estudiante.delete_estudiantemateriacurso'
