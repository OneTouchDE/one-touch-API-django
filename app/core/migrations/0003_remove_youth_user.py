# Generated by Django 4.0.10 on 2024-05-07 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_youth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='youth',
            name='user',
        ),
    ]