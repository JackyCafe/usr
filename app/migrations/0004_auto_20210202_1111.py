# Generated by Django 3.1.3 on 2021-02-02 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_reading_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reading',
            name='slug',
            field=models.SlugField(blank=True, max_length=32, null=True),
        ),
    ]
