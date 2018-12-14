from django.db import models

# Create your models here.

from django.db import models

class Boleta(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    numero_venta = models.IntegerField()

class Inventario(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    id_tienda = models.IntegerField()

class Producto(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=20, unique=True)
    descripcion= models.TextField(null=True, blank=True)
    stock = models.IntegerField()
    precio = models.IntegerField()

class Tienda(models.Model):
    nombre = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=15)
    comuna = models.CharField(max_length=15)
    dirección = models.CharField(max_length=30)

class Vendedor(models.Model):
    rut = models.CharField(primary_key=True, max_length=12)
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    edad = models.IntegerField()
    usuario = models.CharField(max_length=12)
    contraseña = models.CharField(max_length=40)
    correo = models.CharField(max_length=60)
    tienda= models.ForeignKey(Tienda,null=True, blank=True , on_delete=models.CASCADE)

class Venta(models.Model):
    numero = models.IntegerField(primary_key=True)
    fecha = models.DateTimeField()
    cantidad = models.IntegerField()
    total = models.IntegerField()
    rut_vendedor = models.ForeignKey(Vendedor, models.DO_NOTHING,null=True, blank=True, db_column='rut_vendedor')
    comentario = models.CharField(max_length=100, blank=True, null=True)

class Persona(models.Model):
    rut: models.CharField(max_length=13, primary_key=True)
    nombre: models.CharField(max_length=50)
    apellido: models.CharField(max_length=50, null=False)

