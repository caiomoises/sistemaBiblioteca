# Generated by Django 4.2.7 on 2023-11-18 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0002_remove_emprestimo_nome_emprestimo_cliente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateField(),
        ),
    ]
