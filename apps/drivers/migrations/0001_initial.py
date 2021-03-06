# Generated by Django 4.0.1 on 2022-01-14 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('number', models.CharField(max_length=8)),
                ('model', models.CharField(max_length=25)),
                ('color', models.CharField(max_length=25)),
                ('seria_number', models.CharField(max_length=63, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('balance', models.PositiveIntegerField(default=0)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='drivers', to='drivers.car')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
