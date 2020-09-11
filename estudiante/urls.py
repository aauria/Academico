from django.contrib import admin
from django.urls import path
from estudiante import views


urlpatterns = [
    path('formulario/', views.crear_estudiante.as_view(), name="formulario_estudiante"),
    path('consulta/', views.lista_estudiante.as_view(), name="consulta_estudiante"),
    path('editar_estudiante/<int:pk>', views.update_estudiante.as_view(), name="editar_estudiante"),
    path('eliminar_estudiante/<int:pk>', views.delete_estudiante.as_view(), name="eliminar_estudiante"),
    path('formulario1/', views.crear_estudiantedocentemateria.as_view(), name="formulario_estudiante_doc_mat"),
    path('consulta1/', views.lista_estudiantedocentemateria.as_view(), name="consulta_estudiante_doc_mat"),
    path('editar1/<int:pk>', views.update_estudiantedocentemateria.as_view(), name="editar_estudiante_doc_mat"),
    path('eliminar1/<int:pk>', views.delete_estudiantedocentemateria.as_view(), name="eliminar_estudiante_doc_mat"),
    path('admin/', admin.site.urls),
]
