# Generated by Django 4.1 on 2022-09-23 14:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BlogApp', '0004_alter_articulo_nombre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articulo',
            old_name='nombre',
            new_name='subtitulo',
        ),
        migrations.RemoveField(
            model_name='articulo',
            name='cantidad_paginas',
        ),
        migrations.AddField(
            model_name='articulo',
            name='cuerpo',
            field=models.CharField(default='Empty', max_length=700),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='articulos'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='titulo',
            field=models.CharField(default='Empty', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='articulo',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]