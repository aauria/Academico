"""proyectomanual URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include
from django.contrib.auth.urls import views as login
from core import views


urlpatterns = [
    path('', login.LoginView.as_view(template_name='login2.html'),name='login'),
    path('', login.LogoutView.as_view(template_name='login2.html'), name='salir'),
    path('estudiante/',include('estudiante.urls')),
    url('nota/', include('nota.urls')),
    url('materia/', include('materia.urls')),
    url('usuario/', include('usuario.urls')),
    url('curso/', include('curso.urls')),
    path('inicio/', views.home , name="home"),
    path('correo/', views.correo , name="correo"),
    path('exportardocente/', views.exportardocente, name='exportardocente'),
    path('formulario/', views.crear_docente.as_view(), name="formulario"),
    path('consulta/', views.lista_docente.as_view(), name="consulta"),
    path('editar_docente/<int:pk>', views.update_docente.as_view(), name="editar"),
    path('eliminar_docente/<int:pk>', views.delete_docente.as_view(), name="eliminar"),
    path('formulario_docentecurso/', views.crear_docentecurso.as_view(), name="formulario_docentecurso"),
    path('consulta_docentecurso/', views.lista_docentecurso.as_view(), name="consulta_cursodocente"),
    path('editar_docentecurso/<int:pk>', views.update_docentecurso.as_view(), name="editar_docentecurso"),
    path('eliminar_docentecurso/<int:pk>', views.delete_docentecurso.as_view(), name="eliminar_docentecurso"),
    path('admin/', admin.site.urls),
]
