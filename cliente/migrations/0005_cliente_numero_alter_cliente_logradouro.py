# Generated by Django 4.2.7 on 2023-11-14 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_cliente_logradouro'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='Numero',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Logradouro',
            field=models.CharField(max_length=100),
        ),
    ]