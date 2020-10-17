from django.contrib import admin
from django.urls import path
from materia import views


urlpatterns = [
    path('formulario_materia/', views.crear_materia.as_view(), name="formulario_materia"),
    path('consulta_materia/', views.lista_materia.as_view(), name="consulta_materia"),
    path('editar_materia/<int:pk>', views.update_materia.as_view(), name="editar_materia"),
    path('exportarmateria/', views.exportarmateria, name='exportarmateria'),
    path('eliminar_materia/<int:pk>', views.delete_materia.as_view(), name="eliminar_materia"),
    path('admin/', admin.site.urls),
]