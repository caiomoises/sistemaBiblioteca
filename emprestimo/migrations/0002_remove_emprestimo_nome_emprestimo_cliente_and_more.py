# Generated by Django 4.2.7 on 2023-11-18 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0013_alter_cliente_cpf_alter_cliente_contato_and_more'),
        ('livro', '0006_alter_livro_nome_alter_livro_publicação'),
        ('emprestimo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimo',
            name='Nome',
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='cliente',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateField(auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='devolvido',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='livro_emprestado',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='livro.livro'),
            preserve_default=False,
        ),
    ]
