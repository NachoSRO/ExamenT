from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.tiendas.models import Producto,Vendedor
from apps.tiendas.forms import ProductoForm, VendedorForm
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request,'layouts/layout_base.html')

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
    success_url = reverse_lazy()






