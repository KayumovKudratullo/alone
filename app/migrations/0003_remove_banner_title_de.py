# Generated by Django 5.1.2 on 2024-11-01 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_pepsi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='title_de',
        ),
    ]