# Generated by Django 4.2.7 on 2023-11-14 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0007_alter_cliente_logradouro_alter_cliente_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='Logradouro',
            field=models.CharField(default='Sem Logradouro', max_length=60),
        ),
    ]
