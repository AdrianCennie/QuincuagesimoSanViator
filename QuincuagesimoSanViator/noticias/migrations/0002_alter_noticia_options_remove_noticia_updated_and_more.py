# Generated by Django 4.1.2 on 2022-10-20 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='noticia',
            options={'ordering': ['-created'], 'verbose_name': 'noticia', 'verbose_name_plural': 'noticias'},
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='Updated',
        ),
        migrations.AlterField(
            model_name='noticia',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='descripcion',
            field=models.TextField(verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='image',
            field=models.ImageField(upload_to='Noticias', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Título'),
        ),
        migrations.AddField(
            model_name='noticia',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación'),
        ),
    ]
