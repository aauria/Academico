from django.contrib import admin
from django.urls import path
from curso import views


urlpatterns = [
    path('formulario_curso/', views.crear_curso.as_view(), name="formulario_curso"),
    path('consulta_curso/', views.lista_curso.as_view(), name="consulta_curso"),
    path('editar_curso/<int:pk>', views.update_curso.as_view(), name="editar_curso"),
    path('eliminar_curso/<int:pk>', views.delete_curso.as_view(), name="eliminar_curso"),
    path('exportarcurso/', views.exportarcurso, name='exportarcurso'),
    path('admin/', admin.site.urls),
]