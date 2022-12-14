# Generated by Django 4.1.2 on 2022-10-24 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("name", models.CharField(max_length=200)),
                ("user_id", models.CharField(max_length=200)),
                ("followers", models.PositiveSmallIntegerField()),
                ("following", models.PositiveSmallIntegerField()),
                ("friends", models.PositiveSmallIntegerField()),
                ("avatar_url", models.URLField()),
            ],
        ),
    ]
