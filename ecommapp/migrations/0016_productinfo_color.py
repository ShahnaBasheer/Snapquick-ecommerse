# Generated by Django 4.1.3 on 2023-01-14 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0015_remove_productinfo_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinfo',
            name='Color',
            field=models.ManyToManyField(to='ecommapp.color', verbose_name='Color'),
        ),
    ]