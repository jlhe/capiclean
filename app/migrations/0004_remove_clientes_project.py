# Generated by Django 4.2.10 on 2024-04-24 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_clientes_servicio_solicitado_delete_quote_requests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientes',
            name='project',
        ),
    ]
