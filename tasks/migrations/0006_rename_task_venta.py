# Generated by Django 5.0.4 on 2024-05-15 01:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_remove_cliente_identificador'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task',
            new_name='Venta',
        ),
    ]
