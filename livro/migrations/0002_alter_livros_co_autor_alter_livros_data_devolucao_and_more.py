# Generated by Django 5.0.1 on 2024-01-22 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='co_autor',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='livros',
            name='data_devolucao',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='livros',
            name='data_emprestimo',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='livros',
            name='nome_emprestado',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='livros',
            name='tempo_duracao',
            field=models.DateTimeField(blank=True),
        ),
    ]
