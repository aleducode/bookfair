# Generated by Django 2.2.2 on 2019-06-17 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fair', '0004_auto_20190617_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Título')),
                ('number', models.CharField(max_length=500, verbose_name='Número')),
            ],
        ),
    ]