# Generated by Django 5.0.6 on 2024-06-13 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HousesDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_bedrooms', models.IntegerField()),
                ('no_of_bathrooms', models.IntegerField()),
                ('sqrt_feets', models.FloatField()),
                ('price', models.IntegerField()),
                ('desc', models.TextField()),
            ],
        ),
    ]