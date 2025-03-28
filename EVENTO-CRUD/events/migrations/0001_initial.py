# Generated by Django 5.1.7 on 2025-03-14 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=255)),
                ('Descrição', models.TextField()),
                ('Data_Hora', models.DateField()),
                ('Hora', models.TimeField()),
                ('Local', models.CharField(max_length=255)),
                ('Categoria', models.CharField(choices=[('Música', 'Música'), ('Palestra', 'Palestra'), ('Workshop', 'Workshop')], max_length=10)),
            ],
        ),
    ]
