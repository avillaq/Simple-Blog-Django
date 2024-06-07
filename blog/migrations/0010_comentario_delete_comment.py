# Generated by Django 5.0.2 on 2024-06-07 17:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_rename_body_post_cuerpo_rename_status_post_estado_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('cuerpo', models.TextField()),
                ('fecha_creado', models.DateTimeField(auto_now_add=True)),
                ('activo', models.BooleanField(default=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='blog.post')),
            ],
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
