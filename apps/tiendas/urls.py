from django.urls import path, re_path
from . import views
from apps.tiendas.views import index

urlpatterns = [
    path('', index, name= 'index'),
    path('producto/nuevo', views.CrearProducto.as_view(), name='producto_crear'),
    path('producto/listar', views.ListarProducto.as_view(), name='producto_listar'),
    path('producto/editar/<pk>/', views.EditarProducto.as_view(), name='producto_editar'),
    path('producto/eliminar/<pk>/', views.EliminarProducto.as_view(), name='producto_eliminar'),
    path('vendedor/listar', views.ListarVendedor.as_view(), name='vendedor_listar'),
    path('vendedor/nuevo', views.CrearVendedor.as_view(), name='vendedor_crear'),
    path('vendedor/editar/<pk>/', views.EditarVendedor.as_view(), name='vendedor_editar'),
    path('vendedor/eliminar/<pk>/', views.EliminarVendedor.as_view(), name='vendedor_eliminar'),
    path('sucursal/listar', views.ListarTienda.as_view(), name='tienda_listar'),
    path('sucursal/nueva', views.CrearTienda.as_view(), name='tienda_crear'),
    path('sucursal/editar/<pk>/', views.EditarTienda.as_view(), name='tienda_editar'),
    path('sucursal/eliminar/<pk>/', views.EliminarTienda.as_view(), name='tienda_eliminar'),
    path('venta/listar', views.ListarVenta.as_view(), name='venta_listar'),
    path('venta/nueva', views.CrearVenta.as_view(), name='venta_crear'),
    path('venta/editar/<pk>/', views.EditarVenta.as_view(), name='venta_editar'),
    path('venta/eliminar/<pk>/', views.EliminarVenta.as_view(), name='venta_eliminar'),

]