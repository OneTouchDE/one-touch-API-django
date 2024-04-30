# Generated by Django 4.0.10 on 2024-04-30 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Youth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birth_date', models.DateField(auto_now_add=True)),
                ('from_city_germany', models.CharField(max_length=50)),
                ('from_city_india', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('sabha_type', models.CharField(max_length=50)),
            ],
        ),
    ]
