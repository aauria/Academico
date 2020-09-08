from django.contrib.auth.models import User
from usuario.forms import RegistroForms
from django.views.generic import CreateView
from django.urls import reverse_lazy
from core import views


class registro_usuario(CreateView):
    model = User
    template_name = "registrar_usuario.html"
    form_class = RegistroForms
    success_url = reverse_lazy(views.home)

# Create your views here.
