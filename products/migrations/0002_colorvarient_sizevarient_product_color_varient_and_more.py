# Generated by Django 5.1.2 on 2024-10-21 15:07

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ColorVarient",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updateed_at", models.DateTimeField(auto_now_add=True)),
                ("color", models.CharField(max_length=20)),
                ("extra_price", models.IntegerField(default=0)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SizeVarient",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updateed_at", models.DateTimeField(auto_now_add=True)),
                ("size", models.CharField(max_length=20)),
                ("extra_price", models.IntegerField(default=0)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="product",
            name="color_varient",
            field=models.ManyToManyField(blank=True, to="products.colorvarient"),
        ),
        migrations.AddField(
            model_name="product",
            name="size_varient",
            field=models.ManyToManyField(blank=True, to="products.sizevarient"),
        ),
    ]
