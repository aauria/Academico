from django.conf.urls import url
from django.urls import path

from usuario import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'Registra',login_required(views.registro_usuario.as_view()),name='registro_usuario'),
    url(r'Consulta_Usuario', login_required(views.lista_usuario.as_view()), name='consulta_usuario'),
    path('Editar/<int:pk>',login_required( views.update_usuario.as_view()), name='editar_usuario'),
    path('Eliminar/<int:pk>', login_required(views.delete_usuario.as_view()), name='eliminar_usuario'),
    url(r'Grupo', login_required(views.registro_grupo.as_view()), name='registro_grupo'),
    url(r'Consulta', login_required(views.lista_grupo.as_view()), name='consulta_grupo'),
    path('corrige/<int:pk>',login_required( views.update_grupo.as_view()), name='editar_grupo'),
    path('suprimegrupo/<int:pk>', login_required(views.delete_grupo.as_view()), name='eliminar_grupo'),


]