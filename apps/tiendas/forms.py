from django import forms
from apps.tiendas.models import Producto,Vendedor, Tienda, Venta

class ProductoForm(forms.ModelForm):

    class Meta:
            model = Producto

            fields = [

                'id',
                'nombre',
                'stock',
                'precio',
            ]

            labels = {

                'id': 'Id_Producto',
                'nombre': 'Nombre',
                'stock': 'Stock',
                'precio': 'Precio',
            }

            widgets = {

                'id': forms.TextInput(attrs={'class':'form-control'}),
                'nombre': forms.TextInput(attrs={'class':'form-control'}),
                'stock': forms.TextInput(attrs={'class':'form-control'}),
                'precio': forms.TextInput(attrs={'class':'form-control'}),

            }

class VendedorForm(forms.ModelForm):

    class Meta:
            model = Vendedor

            fields = [
                'rut',
                'nombres',
                'apellidos',
                'edad',
                'usuario',
                'contraseña',
                'correo',
                'tienda',
            ]

            labels = {

                'rut': ' Rut',
                'nombres': 'Nombres',
                'apellidos': 'Apellidos',
                'edad': ' Edad',
                'usuario': ' Usuario',
                'contraseña': ' Contraseña',
                'correo': 'Correo',
                'tienda': ' Tienda',
            }

            widgets = {

                'rut': forms.TextInput(attrs={'class':'form-control'}),
                'nombres': forms.TextInput(attrs={'class':'form-control'}),
                'apellidos': forms.TextInput(attrs={'class':'form-control'}),
                'edad': forms.TextInput(attrs={'class':'form-control'}),
                'usuario': forms.TextInput(attrs={'class':'form-control'}),
                'contraseña': forms.PasswordInput(attrs={'class':'form-control'}),
                'correo': forms.TextInput(attrs={'class':'form-control'}),
                'tienda': forms.Select(attrs={'class':'form-control'}),
            }

class TiendaForm(forms.ModelForm):

    class Meta:
            model = Tienda

            fields = [
                'nombre',
                'ciudad',
                'comuna',
                'dirección',
            ]

            labels = {

                'nombre': 'Nombre',
                'ciudad': 'Ciudad',
                'comuna': 'Comuna',
                'dirección': 'direccion',
            }

            widgets = {

                'nombre': forms.TextInput(attrs={'class':'form-control'}),
                'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
                'comuna': forms.TextInput(attrs={'class': 'form-control'}),
                'dirección': forms.TextInput(attrs={'class': 'form-control'}),

            }

class VentaForm(forms.ModelForm):

    class Meta:
            model = Venta

            fields = [

                'numero',
                'fecha',
                'cantidad',
                'total',
                'rut_vendedor',
                'comentario',
            ]

            labels = {

                'numero': 'Numero Venta',
                'fecha': 'Fecha',
                'cantidad': 'Cantidad',
                'total': 'Total',
                'rut_vendedor': 'Rut Vendedor',
                'comentario': 'Comentario',
            }

            widgets = {

                'numero': forms.TextInput(attrs={'class':'form-control'}),
                'fecha': forms.DateInput(attrs={}),
                'cantidad': forms.TextInput(attrs={'class':'form-control'}),
                'total': forms.TextInput(attrs={'class':'form-control'}),
                'rut_vendedor': forms.TextInput(attrs={'class':'form-control'}),
                'comentario': forms.TextInput(attrs={'class':'form-control'}),

            }