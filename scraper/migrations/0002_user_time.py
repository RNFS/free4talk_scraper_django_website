# Generated by Django 4.0.6 on 2022-10-25 13:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
