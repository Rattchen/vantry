# Generated by Django 4.1.2 on 2025-04-12 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("off_id", models.PositiveBigIntegerField(blank=True, null=True)),
                ("brand", models.CharField(max_length=250)),
                ("name", models.CharField(max_length=250)),
                ("calories", models.PositiveIntegerField()),
                ("expiry_date", models.DateField(blank=True, null=True)),
            ],
        ),
    ]
