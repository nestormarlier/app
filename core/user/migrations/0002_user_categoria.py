# Generated by Django 3.0.4 on 2021-04-11 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='categoria',
            field=models.TextField(choices=[('SUPERVISOR', 'SUPERVISOR'), ('MAQUINISTA', 'MAQUINISTA'), ('1ER AYUDANTE', '1ER AYUDANTE'), ('2DO AYUDANTE', '2DO AYUDANTE'), ('MECANICO', 'MECÁNICO')], default=1),
            preserve_default=False,
        ),
    ]
