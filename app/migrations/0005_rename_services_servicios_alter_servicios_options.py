# Generated by Django 4.2.10 on 2024-04-24 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_clientes_project'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='services',
            new_name='Servicios',
        ),
        migrations.AlterModelOptions(
            name='servicios',
            options={'verbose_name': 'Servicio', 'verbose_name_plural': 'Servicios'},
        ),
    ]
