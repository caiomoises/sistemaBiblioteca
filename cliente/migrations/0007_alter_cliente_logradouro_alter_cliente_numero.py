# Generated by Django 4.2.7 on 2023-11-14 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0006_alter_cliente_logradouro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='Logradouro',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Numero',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
