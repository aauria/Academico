from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import Estudiante
from .form import Estudianteform
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

