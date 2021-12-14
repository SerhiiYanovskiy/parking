# Generated by Django 4.0 on 2021-12-14 19:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First_name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last_name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=100, verbose_name='Make')),
                ('model', models.CharField(max_length=100, verbose_name='Model')),
                ('plate_number', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator('[A-Я]{2}\\s[0-9]{4}\\s[A-Я]{2}')], verbose_name='Plate_number')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('driver_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='driver', to='parkingapp.driver', verbose_name='Driver')),
            ],
        ),
    ]