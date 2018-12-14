from django.urls import path, re_path
from . import views
from apps.auth.views import RegistroUsuario


urlpatterns = [
    path('registrar', RegistroUsuario, name='registro_usuario')

]