from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.tiendas.models import Producto,Vendedor, Tienda, Venta
from apps.tiendas.forms import ProductoForm, VendedorForm, TiendaForm, VentaForm
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request,'common/index.html')

class ListarProducto(ListView):
    model = Producto
    template_name = 'producto/producto_listar.html'

class CrearProducto(CreateView):
    model= Producto
    form_class = ProductoForm
    template_name = 'producto/producto_form.html'
    success_url = reverse_lazy('producto_listar')

class EditarProducto(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/producto_form.html'
    success_url = reverse_lazy('producto_listar')

class EliminarProducto(DeleteView):
    model = Producto
    template_name = 'producto/producto_eliminar.html'
    success_url = reverse_lazy('producto_listar')


class ListarVendedor(ListView):
    model = Vendedor
    template_name = 'vendedor/vendedor_listar.html'

class CrearVendedor(CreateView):
    model = Vendedor
    form_class = VendedorForm
    template_name = 'vendedor/vendedor_form.html'
    success_url = reverse_lazy('vendedor_listar')

class EditarVendedor(UpdateView):
    model = Vendedor
    form_class = VendedorForm
    template_name = 'vendedor/vendedor_form.html'
    success_url = reverse_lazy('vendedor_listar')

class EliminarVendedor(DeleteView):
    model = Vendedor
    template_name = 'vendedor/vendedor_eliminar.html'
    success_url = reverse_lazy('vendedor_listar')


class ListarTienda(ListView):
    model = Tienda
    template_name = 'tiendas/tienda_listar.html'

class CrearTienda(CreateView):
    model = Tienda
    form_class = TiendaForm
    template_name = 'tiendas/tienda_form.html'
    success_url = reverse_lazy('tienda_listar')

class EditarTienda(UpdateView):
    model = Tienda
    form_class = TiendaForm
    template_name = 'tiendas/tienda_form.html'
    success_url = reverse_lazy('tienda_listar')

class EliminarTienda(DeleteView):
    model = Tienda
    template_name = 'tiendas/tienda_eliminar.html'
    success_url = reverse_lazy('tienda_listar')


class ListarVenta(ListView):
    model = Venta
    template_name = 'ventas/ventas_listar.html'

class CrearVenta(CreateView):
    model = Venta
    form_class = VentaForm
    template_name = 'ventas/ventas_form.html'
    success_url = reverse_lazy('index')

class EditarVenta(UpdateView):
    model = Venta
    form_class = VentaForm
    template_name = 'tiendas/tienda_form.html'
    success_url = reverse_lazy('venta_listar')

class EliminarVenta(DeleteView):
    model = Venta
    template_name = 'tiendas/tienda_eliminar.html'
    success_url = reverse_lazy('tienda_listar')






