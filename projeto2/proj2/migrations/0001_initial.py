# Generated by Django 4.2.10 on 2024-02-08 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calca', models.IntegerField()),
                ('blusa', models.IntegerField()),
                ('saia', models.IntegerField()),
                ('bone', models.IntegerField()),
            ],
        ),
    ]
