# Generated by Django 3.2.8 on 2024-10-04 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('imagen', models.ImageField(null=True, upload_to='imagenes/', verbose_name='Título')),
                ('description', models.TextField(null=True, verbose_name='Descripción')),
            ],
        ),
    ]
