from datetime import datetime
import datetime
from django.utils import timezone
from core.user.models import User
from django.db import models
from django.forms import model_to_dict

from config.settings import MEDIA_URL, STATIC_URL
from core.erp.choices import gender_choices
from core.models import BaseModel

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    desc = models.CharField(max_length=500, null=True, blank=True, verbose_name='Descripción')

    def __str__(self):
        return self.name
        
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoría')
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen')
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio de venta')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['cat'] = self.cat.toJSON()
        item['image'] = self.get_image()
        item['pvp'] = format(self.pvp, '.2f')
        return item

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

class Client(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    surnames = models.CharField(max_length=150, verbose_name='Apellidos')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    date_birthday = models.DateField(default=timezone.now, verbose_name='Fecha de nacimiento')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    gender = models.CharField(max_length=10, choices=gender_choices, default='male', verbose_name='Sexo')

    def __str__(self):
        return self.names

    def toJSON(self):
        item = model_to_dict(self)
        item['gender'] = {'id': self.gender, 'name': self.get_gender_display()}
        item['date_birthday'] = self.date_birthday.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']

class Sale(models.Model):
    cli = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_joined = models.DateField(default=timezone.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cli.names

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']

class DetSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prod.name

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        ordering = ['id']

class FichaTecnica(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    active = models.BooleanField(
        verbose_name='Ficha Técnica Activo', default=True)

    created = models.DateTimeField(
        verbose_name='Fecha de alta', auto_now_add=True, db_column='creado')
    modified = models.DateTimeField(
        verbose_name='Fecha modificado', auto_now=True, db_column='modificado')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # EN NULO SI SIGUE ACTIVO
    delete = models.DateField(verbose_name='Fecha baja', null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Ficha Técnica'
        verbose_name_plural = 'Fichas Técnicas'
        db_table = 'ficha_tecnica'
        ordering = ['id']

    def  toJSON(self):
        item = model_to_dict(self)
        return item

class Impresora(models.Model):
    impresora_id = models.IntegerField(primary_key=True, verbose_name='Número')
    nombre = models.CharField(max_length=30, unique= True)

    created = models.DateTimeField(
        verbose_name='Fecha de alta', auto_now_add=True, db_column='creado')
    modified = models.DateTimeField(
        verbose_name='Fecha modificado', auto_now=True, db_column='modificado')

    activo = models.BooleanField(verbose_name='Impresora Activa', default=True)
    # EN NULO SI SIGUE ACTIVO

    def __str__(self):
        return "%s" % self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'impresora'
        ordering = ['impresora_id']

class Parada(models.Model):
    NOMBRE_CHOICES = [
        ('TINTAS', 'TINTAS'),
        ('MONTAJE', 'MONTAJE'),
        ('DEPÓSITO', 'DEPÓSITO'),
        ('MANTENIMIENTO', 'MANTENIMIENTO'),
        ('PROGRAMACIÓN', 'PROGRAMACIÓN'),
        ('SUPERVICIÓN', 'SUPERVICIÓN'),
        ('PRODUCCIÓN', 'PRODUCCIÓN'),
        ('OPERATIVO', 'OPERATIVO'),
        ('CALIDAD', 'CALIDAD')
    ]
    #parada_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, unique=True)

    created = models.DateTimeField(
        verbose_name='Fecha de alta', auto_now_add=True, db_column='creado')
    modified = models.DateTimeField(
        verbose_name='Fecha modificado', auto_now=True, db_column='modificado')

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    active = models.BooleanField(
        verbose_name='Ficha Técnica Activo', default=True)
    sector_asignado = models.CharField(max_length=30, choices=NOMBRE_CHOICES)
    # EN NULO SI SIGUE ACTIVO
    delete = models.DateField(verbose_name='Fecha baja', null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'parada'
        ordering = ['id']

    def toJSON(self):
        item = model_to_dict(self)
        return item

class CambioMecanico(models.Model):
    #cambio_id = models.AutoField(primary_key=True)
    create = models.DateTimeField(
        verbose_name='Fecha creación', null=True, blank=True, default=datetime.datetime.now)
    modified = models.DateTimeField(
        verbose_name='Fecha modificado', auto_now=True, db_column='modificado')
    parada = models.ForeignKey(
        Parada, verbose_name='Parada', on_delete=models.CASCADE, null=True, blank=True)
    fecha_fin = models.DateTimeField(verbose_name='Fin cambio')

    class Meta:
        verbose_name = 'Cambio mecánico'
        verbose_name_plural = 'Cambios Mecánicos'
        db_table = 'cambio_mecanico'

    def __str__(self):
        return str(self.parada)

    def toJSON(self):
        item = model_to_dict(self)
        return item

class Setup(models.Model):
    create = models.DateTimeField(
        verbose_name='Fecha creación', null=True, blank=True, default=datetime.datetime.now)
    parada = models.ForeignKey(
        Parada, verbose_name='Parada', on_delete=models.CASCADE, null=True, blank=True)
    fecha_fin = models.DateTimeField(verbose_name='Fin Setup')

    class Meta:
        verbose_name = 'Setup'
        verbose_name_plural = 'Setups'
        db_table = 'setup'

    def __str__(self):
        return str(self.parada)

    def toJSON(self):
        item = model_to_dict(self)
        return item

class Produccion(models.Model):
    #produccion_id = models.AutoField(primary_key=True)
    create = models.DateTimeField(
        verbose_name='Fecha de creación', null=True, blank=True, default=datetime.datetime.now)
    parada = models.ForeignKey(
        Parada, verbose_name='Parada', on_delete=models.CASCADE, null=True, blank=True)
    fecha_fin = models.DateTimeField(verbose_name='Fin producción')

    class Meta:
        verbose_name = 'Producción'
        verbose_name_plural = 'Producciones'
        db_table = 'produccion'

    def __str__(self):
        return str(self.parada)

    def toJSON(self):
        item = model_to_dict(self)
        return item

class ObservacionesGles(models.Model):
        #produccion_id = models.AutoField(primary_key=True)
    create = models.DateTimeField(
        verbose_name='Fecha de creación', null=True, blank=True, default=datetime.datetime.now)
    observacion = models.TextField(verbose_name='Observaciones generales', null=True, blank=True)
    fecha_fin = models.DateTimeField(verbose_name='Fin observación')

    class Meta:
        verbose_name = 'Observación general'
        verbose_name_plural = 'Observaciones generales'
        db_table = 'observaciones_gles'

    def __str__(self):
        return str(self.observacion)

    def toJSON(self):
        item = model_to_dict(self)
        return item

class ObsMantenimiento(models.Model):
    #produccion_id = models.AutoField(primary_key=True)
    mecanico = models.ForeignKey(User, verbose_name='Mecánico', on_delete=models.DO_NOTHING, related_name='mecanico', db_column='mecanico')
    create = models.DateTimeField(
        verbose_name='Fecha de creación', null=True, blank=True, default=datetime.datetime.now)
    observacion = models.TextField(verbose_name='Observaciones del mecánico', null=True, blank=True)

    class Meta:
        verbose_name = 'Observación mantenimiento'
        verbose_name_plural = 'Observaciones mantenimiento'
        db_table = 'observaciones_mant'

    def __str__(self):
        return str(self.observacion)

    def toJSON(self):
        item = model_to_dict(self)
        return item

class PedidoVenta(models.Model):
    create = models.DateField(verbose_name='Fecha creación', auto_now_add=True)
    fecha_entrega = models.DateField(verbose_name="Fecha de entrega")
    fichaTecnica = models.ForeignKey(FichaTecnica, on_delete=models.CASCADE)
    kg_prod = models.DecimalField(default=0, max_digits=9, decimal_places=0, verbose_name="Kg. a producir")

    class Meta:
        verbose_name = 'Pedido de Venta'
        verbose_name_plural = 'Pedidos de Venta'
        db_table = 'pedido_venta'
    
    def __str__(self):
        return 'Pedido de Venta Nro.' + str(self.id) + ' - ' + str(self.fichaTecnica) + ' - ' + str(self.kg_prod) + 'Kg.' + ' - ' + 'Fecha de entrega ' + str(self.fecha_entrega)

    def toJSON(self):
        item = model_to_dict(self)
        return item

class OrdenesProduccion(models.Model):
    create = models.DateField(verbose_name='Fecha creación', auto_now_add=True)
    pedido_venta = models.ForeignKey(PedidoVenta, on_delete = models.CASCADE)
    impresora = models.ForeignKey(Impresora, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Ordenes de producción'
        verbose_name_plural = 'Ordenes de producción'
        db_table = 'orden_produccion'
    
    def __str__(self):
        return 'Orden de Prod. Nro.' + str(self.id) + ' - ' + str(self.impresora) + ' - ' + str(self.pedido_venta)
    
    def toJSON(self):
        item = model_to_dict(self)
        item['pedido_venta']= self.pedido_venta.toJSON()
        item['impresora']= self.impresora.toJSON()
        return item

class ParteImpresion(models.Model):
    #parte_id = models.AutoField(verbose_name='Orden impresión', primary_key=True)

    ordenes = models.ForeignKey(OrdenesProduccion, on_delete=models.CASCADE)

    maquinista = models.ForeignKey(User, verbose_name='Maquinista', on_delete=models.DO_NOTHING,
                                   related_name='maquinista', db_column='maquinista')
    supervisor = models.ForeignKey(User, verbose_name='Supervisor', on_delete=models.DO_NOTHING,
                                   related_name='supervisor', db_column='supervisor')
    ayudante1ero = models.ForeignKey(User, verbose_name='Primer ayudante', on_delete=models.DO_NOTHING,
                                     related_name='ayudante1er', db_column='ayudante1er')
    ayudante2do = models.ForeignKey(User, verbose_name='Segundo ayudante', on_delete=models.DO_NOTHING,
                                    related_name='ayudante2do', db_column='ayudante2do')
    create = models.DateField(verbose_name='Fecha creación', auto_now_add=True)

    cambio = models.ManyToManyField(CambioMecanico, verbose_name="Cambio Mecánico", related_name='cambio',
                                    db_column='cambio_id', blank=True)
    setup = models.ManyToManyField(Setup, verbose_name='RM AC AP', related_name='setup', db_column='setup',
                                   blank=True)
    produccion = models.ManyToManyField(Produccion, verbose_name='Producción', related_name='produccion',
                                        db_column='produccion', blank=True)
    observacion_gral = models.ManyToManyField(ObservacionesGles, verbose_name = 'Observaciones generales', related_name= 'observacion_gral', db_column='obs_gles', blank=True)
    observacion_mant = models.ManyToManyField(ObsMantenimiento, verbose_name='Observaciones de mantenimiento', related_name='observacion_mant', db_column='obs_mant', blank=True)

    metros_registro = models.IntegerField(verbose_name='Metros registro')
    kg_registro = models.IntegerField(verbose_name='Kg. registro')
    metros = models.IntegerField(verbose_name='Metros producidos')
    kg = models.IntegerField(verbose_name='Kg producidos')

    class Meta:
        verbose_name = 'Parte de impresión'
        verbose_name_plural = 'Partes de impresión'
        db_table = 'parte_impresion'

    def __str__(self):
        return str(self.id)

    def toJSON(self):
        item = model_to_dict(self)

        # POST dicccionario con las paradas en los cambios
        item['cambio'] = [model_to_dict(c) for c in self.cambio.all()]

        # POST dicccionario con las paradas en los setups
        item['setup'] = [model_to_dict(s) for s in self.setup.all()]
        
        # POST dicccionario con las paradas en lo producción
        item['produccion'] = [model_to_dict(p) for p in self.produccion.all()]
        
        return item