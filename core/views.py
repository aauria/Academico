from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import Docente,CursoDocente
from .form import Docenteform,CursoDocenteForm
from django.views.generic import ListView,CreateView,DeleteView,UpdateView


# relaciona la parte vista con el template home.html
def home(request, plantilla="home.html"):
    return render(request, plantilla);
def index(request, plantilla="index.html"):
    return render(request, plantilla);
def login(request, plantilla="login.html"):
    return render(request, plantilla);
def correo(request, plantilla="correo.html"):
    return render(request, plantilla);

class lista_docente(ListView):
    model = Docente
    template_name = 'consulta.html'

class crear_docente(CreateView):
    model = Docente
    form_class = Docenteform
    template_name = 'formulario.html'
    success_url = reverse_lazy('home')

class update_docente(UpdateView):
    model = Docente
    form_class = Docenteform
    template_name = 'formulario.html'
    success_url = reverse_lazy('consulta')

class delete_docente(DeleteView):
    model = Docente
    template_name = 'verificar.html'
    success_url = reverse_lazy('consulta')

class lista_docentecurso(ListView):
    model = CursoDocente
    template_name = 'consulta_cursodocente.html'

class crear_docentecurso(CreateView):
    model = CursoDocente
    form_class = CursoDocenteForm
    template_name = 'formulario_cursodocente.html'
    success_url = reverse_lazy('home')

class update_docentecurso(UpdateView):
    model = CursoDocente
    form_class = CursoDocenteForm
    template_name = 'formulario_cursodocente.html'
    success_url = reverse_lazy('consulta_cursodocente')

class delete_docentecurso(DeleteView):
    model = CursoDocente
    template_name = 'verificar_cursodocente.html'
    success_url = reverse_lazy('consulta_cursodocente')
# Create your views here.
