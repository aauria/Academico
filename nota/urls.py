from django.contrib import admin
from django.urls import path
from nota import views


urlpatterns = [
    path('formulario_nota/', views.crear_notas.as_view(), name="formulario_nota"),
    path('consulta_nota/', views.lista_notas.as_view(), name="consulta_nota"),
    path('editar_nota/<int:pk>', views.update_notas.as_view(), name="editar_nota"),
    path('eliminar_nota/<int:pk>', views.delete_notas.as_view(), name="eliminar_nota"),
    path('admin/', admin.site.urls),
]