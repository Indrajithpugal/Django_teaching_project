# Generated by Django 5.0.6 on 2024-06-25 12:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groceries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('rating', models.FloatField()),
                ('review', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grocery_image', models.FileField(upload_to='grocery_images')),
                ('grocery_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drfviews.groceries')),
            ],
        ),
    ]
