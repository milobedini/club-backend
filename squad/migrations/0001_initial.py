# Generated by Django 4.1b1 on 2022-06-21 11:33

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Squad",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("sport", models.CharField(max_length=100)),
                ("recurring", models.BooleanField(default=False)),
                ("venue", models.CharField(blank=True, default=None, max_length=100)),
                ("weekday", models.CharField(blank=True, default=None, max_length=100)),
                (
                    "image",
                    cloudinary.models.CloudinaryField(
                        default="", max_length=255, verbose_name="image"
                    ),
                ),
            ],
        ),
    ]
