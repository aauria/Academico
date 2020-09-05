from django.conf.urls import url
from usuario import views


urlpatterns = [
    url('Registra',views.registro_usuario.as_view(), name="crear_usuario"),

]