# Generated by Django 4.1.3 on 2022-12-05 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0062_allfashion_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allfashion',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
    ]
