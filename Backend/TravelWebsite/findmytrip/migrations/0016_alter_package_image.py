# Generated by Django 5.0.1 on 2024-04-03 00:26

import TravelWebsite.findmytrip.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findmytrip', '0015_remove_package_activities_remove_package_flights_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='image',
            field=models.ImageField(blank=True, default='media/default_image.jpg', upload_to=TravelWebsite.findmytrip.models.upload_path),
        ),
    ]
