# Generated by Django 5.0.6 on 2024-06-20 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=40)),
                ('os_type', models.CharField(max_length=40)),
                ('size', models.FloatField(default=14)),
                ('color', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
