from django.contrib import admin
from django.urls import path
from estudiante import views


urlpatterns = [
    path('', views.login , name="login"),
    path('/inicio', views.home , name="home"),
    path('/correo', views.correo , name="correo"),
    path('/formulario', views.crear_estudiante.as_view(), name="formulario_estudiante"),
    path('/consulta', views.lista_estudiante.as_view(), name="consulta_estudiante"),
    path('/editar_estudiante/<int:pk>', views.update_estudiante.as_view(), name="editar_estudiante"),
    path('/eliminar_estudiante/<int:pk>', views.delete_estudiante.as_view(), name="eliminar_estudiante"),
    path('admin/', admin.site.urls),
]
