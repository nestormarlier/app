# Generated by Django 3.0.4 on 2021-04-20 00:44

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('erp', '0003_auto_20210326_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='CambioMecanico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Fecha creación')),
                ('modified', models.DateTimeField(auto_now=True, db_column='modificado', verbose_name='Fecha modificado')),
                ('fecha_fin', models.DateTimeField(verbose_name='Fin cambio')),
            ],
            options={
                'verbose_name': 'Cambio mecánico',
                'verbose_name_plural': 'Cambios Mecánicos',
                'db_table': 'cambio_mecanico',
            },
        ),
        migrations.CreateModel(
            name='FichaTecnica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('active', models.BooleanField(default=True, verbose_name='Ficha Técnica Activo')),
                ('created', models.DateTimeField(auto_now_add=True, db_column='creado', verbose_name='Fecha de alta')),
                ('modified', models.DateTimeField(auto_now=True, db_column='modificado', verbose_name='Fecha modificado')),
                ('delete', models.DateField(blank=True, null=True, verbose_name='Fecha baja')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ficha Técnica',
                'verbose_name_plural': 'Fichas Técnicas',
                'db_table': 'ficha_tecnica',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Impresora',
            fields=[
                ('impresora_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Número')),
                ('nombre', models.CharField(max_length=30, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_column='creado', verbose_name='Fecha de alta')),
                ('modified', models.DateTimeField(auto_now=True, db_column='modificado', verbose_name='Fecha modificado')),
                ('activo', models.BooleanField(default=True, verbose_name='Impresora Activa')),
            ],
            options={
                'db_table': 'impresora',
                'ordering': ['impresora_id'],
            },
        ),
        migrations.CreateModel(
            name='ObservacionesGles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Fecha de creación')),
                ('observacion', models.TextField(blank=True, null=True, verbose_name='Observaciones generales')),
                ('fecha_fin', models.DateTimeField(verbose_name='Fin observación')),
            ],
            options={
                'verbose_name': 'Observación general',
                'verbose_name_plural': 'Observaciones generales',
                'db_table': 'observaciones_gles',
            },
        ),
        migrations.CreateModel(
            name='ObsMantenimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Fecha de creación')),
                ('observacion', models.TextField(blank=True, null=True, verbose_name='Observaciones del mecánico')),
                ('mecanico', models.ForeignKey(db_column='mecanico', on_delete=django.db.models.deletion.DO_NOTHING, related_name='mecanico', to=settings.AUTH_USER_MODEL, verbose_name='Mecánico')),
            ],
            options={
                'verbose_name': 'Observación mantenimiento',
                'verbose_name_plural': 'Observaciones mantenimiento',
                'db_table': 'observaciones_mant',
            },
        ),
        migrations.CreateModel(
            name='OrdenesProduccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateField(auto_now_add=True, verbose_name='Fecha creación')),
                ('impresora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.Impresora')),
            ],
            options={
                'verbose_name': 'Ordenes de producción',
                'verbose_name_plural': 'Ordenes de producción',
                'db_table': 'orden_produccion',
            },
        ),
        migrations.CreateModel(
            name='Parada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_column='creado', verbose_name='Fecha de alta')),
                ('modified', models.DateTimeField(auto_now=True, db_column='modificado', verbose_name='Fecha modificado')),
                ('active', models.BooleanField(default=True, verbose_name='Ficha Técnica Activo')),
                ('sector_asignado', models.CharField(choices=[('TINTAS', 'TINTAS'), ('MONTAJE', 'MONTAJE'), ('DEPÓSITO', 'DEPÓSITO'), ('MANTENIMIENTO', 'MANTENIMIENTO'), ('PROGRAMACIÓN', 'PROGRAMACIÓN'), ('SUPERVICIÓN', 'SUPERVICIÓN'), ('PRODUCCIÓN', 'PRODUCCIÓN'), ('OPERATIVO', 'OPERATIVO'), ('CALIDAD', 'CALIDAD')], max_length=30)),
                ('delete', models.DateField(blank=True, null=True, verbose_name='Fecha baja')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'parada',
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='client',
            name='date_birthday',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='date_joined',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='Setup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Fecha creación')),
                ('fecha_fin', models.DateTimeField(verbose_name='Fin Setup')),
                ('parada', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp.Parada', verbose_name='Parada')),
            ],
            options={
                'verbose_name': 'Setup',
                'verbose_name_plural': 'Setups',
                'db_table': 'setup',
            },
        ),
        migrations.CreateModel(
            name='Produccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Fecha de creación')),
                ('fecha_fin', models.DateTimeField(verbose_name='Fin producción')),
                ('parada', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp.Parada', verbose_name='Parada')),
            ],
            options={
                'verbose_name': 'Producción',
                'verbose_name_plural': 'Producciones',
                'db_table': 'produccion',
            },
        ),
        migrations.CreateModel(
            name='PedidoVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateField(auto_now_add=True, verbose_name='Fecha creación')),
                ('fecha_entrega', models.DateField(verbose_name='Fecha de entrega')),
                ('kg_prod', models.DecimalField(decimal_places=0, default=0, max_digits=9, verbose_name='Kg. a producir')),
                ('fichaTecnica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.FichaTecnica')),
            ],
            options={
                'verbose_name': 'Pedido de Venta',
                'verbose_name_plural': 'Pedidos de Venta',
                'db_table': 'pedido_venta',
            },
        ),
        migrations.CreateModel(
            name='ParteImpresion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateField(auto_now_add=True, verbose_name='Fecha creación')),
                ('metros_registro', models.IntegerField(verbose_name='Metros registro')),
                ('kg_registro', models.IntegerField(verbose_name='Kg. registro')),
                ('metros', models.IntegerField(verbose_name='Metros producidos')),
                ('kg', models.IntegerField(verbose_name='Kg producidos')),
                ('ayudante1ero', models.ForeignKey(db_column='ayudante1er', on_delete=django.db.models.deletion.DO_NOTHING, related_name='ayudante1er', to=settings.AUTH_USER_MODEL, verbose_name='Primer ayudante')),
                ('ayudante2do', models.ForeignKey(db_column='ayudante2do', on_delete=django.db.models.deletion.DO_NOTHING, related_name='ayudante2do', to=settings.AUTH_USER_MODEL, verbose_name='Segundo ayudante')),
                ('cambio', models.ManyToManyField(blank=True, db_column='cambio_id', related_name='cambio', to='erp.CambioMecanico', verbose_name='Cambio Mecánico')),
                ('maquinista', models.ForeignKey(db_column='maquinista', on_delete=django.db.models.deletion.DO_NOTHING, related_name='maquinista', to=settings.AUTH_USER_MODEL, verbose_name='Maquinista')),
                ('observacion_gral', models.ManyToManyField(blank=True, db_column='obs_gles', related_name='observacion_gral', to='erp.ObservacionesGles', verbose_name='Observaciones generales')),
                ('observacion_mant', models.ManyToManyField(blank=True, db_column='obs_mant', related_name='observacion_mant', to='erp.ObsMantenimiento', verbose_name='Observaciones de mantenimiento')),
                ('ordenes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.OrdenesProduccion')),
                ('produccion', models.ManyToManyField(blank=True, db_column='produccion', related_name='produccion', to='erp.Produccion', verbose_name='Producción')),
                ('setup', models.ManyToManyField(blank=True, db_column='setup', related_name='setup', to='erp.Setup', verbose_name='RM AC AP')),
                ('supervisor', models.ForeignKey(db_column='supervisor', on_delete=django.db.models.deletion.DO_NOTHING, related_name='supervisor', to=settings.AUTH_USER_MODEL, verbose_name='Supervisor')),
            ],
            options={
                'verbose_name': 'Parte de impresión',
                'verbose_name_plural': 'Partes de impresión',
                'db_table': 'parte_impresion',
            },
        ),
        migrations.AddField(
            model_name='ordenesproduccion',
            name='pedido_venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.PedidoVenta'),
        ),
        migrations.AddField(
            model_name='cambiomecanico',
            name='parada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp.Parada', verbose_name='Parada'),
        ),
    ]
