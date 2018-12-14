from django.urls import path, re_path
from . import views
from apps.tiendas.views import index

urlpatterns = [
    path('', index),
    path('producto/nuevo', views.CrearProducto.as_view(), name='producto_crear'),
    path('producto/listar', views.ListarProducto.as_view(), name='producto_listar'),
    path('producto/editar/<pk>/', views.EditarProducto.as_view(), name='producto_editar'),
    path('producto/eliminar/<pk>/', views.EliminarProducto.as_view(), name='producto_eliminar'),
    path('vendedor/listar', views.ListarVendedor.as_view(), name='vendedor_listar'),
    path('vendedor/nuevo', views.CrearVendedor.as_view(), name='vendedor_crear'),

]