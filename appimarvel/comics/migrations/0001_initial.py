# Generated by Django 4.1.1 on 2023-04-24 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('identificacion', models.CharField(max_length=20)),
                ('correo_electronico', models.EmailField(max_length=254)),
            ],
        ),
    ]