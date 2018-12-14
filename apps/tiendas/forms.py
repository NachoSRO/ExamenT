from django import forms
from apps.tiendas.models import Producto,Vendedor

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
                'nombre': forms.TextInput(attrs={'class':'form-control'}),
                'apellidos': forms.TextInput(attrs={'class':'form-control'}),
                'edad': forms.TextInput(attrs={'class':'form-control'}),
                'usuario': forms.TextInput(attrs={'class':'form-control'}),
                'contraseña': forms.PasswordInput(attrs={'class':'form-control'}),
                'correo': forms.EmailInput(attrs={'class':'form-control'}),
                'tienda': forms.TextInput(attrs={'class':'form-control'}),
            }

