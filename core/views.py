from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import Docente,CursoDocente
from .form import Docenteform,CursoDocenteForm
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin


# relaciona la parte vista con el template home.html
def home(request, plantilla="home.html"):
    return render(request, plantilla);
def index(request, plantilla="index.html"):
    return render(request, plantilla);
def login(request, plantilla="login.html"):
    return render(request, plantilla);
def correo(request, plantilla="correo.html"):
    return render(request, plantilla);

class lista_docente(PermissionRequiredMixin,ListView):
    model = Docente
    template_name = 'docente/consulta.html'
    permission_required = 'core.view_docente'

class crear_docente(PermissionRequiredMixin,CreateView):
    model = Docente
    form_class = Docenteform
    template_name = 'docente/formulario.html'
    success_url = reverse_lazy('consulta')
    permission_required = 'core.add_docente'

class update_docente(PermissionRequiredMixin,UpdateView):
    model = Docente
    form_class = Docenteform
    template_name = 'docente/formulario.html'
    success_url = reverse_lazy('consulta')
    permission_required = 'core.change_docente'

class delete_docente(PermissionRequiredMixin,DeleteView):
    model = Docente
    template_name = 'docente/verificar.html'
    success_url = reverse_lazy('consulta')
    permission_required = 'core.delete_docente'

class lista_docentecurso(PermissionRequiredMixin,ListView):
    model = CursoDocente
    template_name = 'curso/consulta_cursodocente.html'
    permission_required = 'core.view_cursodocente'

class crear_docentecurso(PermissionRequiredMixin,CreateView):
    model = CursoDocente
    form_class = CursoDocenteForm
    template_name = 'curso/formulario_cursodocente.html'
    success_url = reverse_lazy('consulta_cursodocente')
    permission_required = 'core.add_cursodocente'

class update_docentecurso(PermissionRequiredMixin,UpdateView):
    model = CursoDocente
    form_class = CursoDocenteForm
    template_name = 'curso/formulario_cursodocente.html'
    success_url = reverse_lazy('consulta_cursodocente')
    permission_required = 'core.change_cursodocente'

class delete_docentecurso(PermissionRequiredMixin,DeleteView):
    model = CursoDocente
    template_name = 'curso/verificar_cursodocente.html'
    success_url = reverse_lazy('consulta_cursodocente')
    permission_required = 'core.delete_cursodocente'
# Create your views here.
