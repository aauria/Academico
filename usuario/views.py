from django.contrib.auth.models import User,Group
from usuario.forms import RegistroForms,GroupForms
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy




class registro_usuario(PermissionRequiredMixin,CreateView):
    model = User
    template_name = "usuario/registrar_usuario.html"
    form_class = RegistroForms
    success_url = reverse_lazy("consulta_usuario")
    permission_required = 'user.add_user'

class lista_usuario(PermissionRequiredMixin,ListView):
    model = User
    template_name = "usuario/consulta_usuario.html"
    permission_required = 'user.view_user'

class update_usuario(PermissionRequiredMixin,UpdateView):
    model = User
    template_name = 'usuario/registrar_usuario.html'
    form_class = RegistroForms
    success_url = reverse_lazy('consulta_usuario')
    permission_required = 'user.change_user'

class delete_usuario(PermissionRequiredMixin,DeleteView):
    model = User
    template_name = 'usuario/verificar_usuario.html'
    success_url = reverse_lazy('consulta_usuario')
    permission_required = 'user.delete_user'

class registro_grupo(PermissionRequiredMixin,CreateView):
    model = Group
    template_name = "usuario/registro_grupo.html"
    form_class = GroupForms
    success_url = reverse_lazy("home")
    permission_required =  'group.add_group'

class lista_grupo(PermissionRequiredMixin,ListView):
    model = Group
    template_name = "usuario/consulta_grupo.html"
    permission_required = 'group.view_group'

class update_grupo(PermissionRequiredMixin,UpdateView):
    model = User
    template_name = 'usuario/registro_grupo.html'
    form_class = GroupForms
    success_url = reverse_lazy('consulta_grupo')
    permission_required = 'group.change_group'

class delete_grupo(PermissionRequiredMixin,DeleteView):
    model = User
    template_name = 'usuario/verificar_grupo.html'
    success_url = reverse_lazy('consulta_grupo')
    permission_required = 'group.delete_group'

