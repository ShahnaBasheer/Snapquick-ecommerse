# Generated by Django 4.1.1 on 2022-09-24 09:27

from django.db import migrations, models
import django.db.models.deletion
import ecomapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoysCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boys', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GirlsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('girls', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MenCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('men', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WomenCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('women', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WomenFashion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('card_image', models.ImageField(upload_to=ecomapp.models.user_directory_path)),
                ('upload_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.womencategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MenFashion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('card_image', models.ImageField(upload_to=ecomapp.models.user_directory_path)),
                ('upload_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.mencategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GirlsFashion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('card_image', models.ImageField(upload_to=ecomapp.models.user_directory_path)),
                ('upload_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.girlscategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BoysFashion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('card_image', models.ImageField(upload_to=ecomapp.models.user_directory_path)),
                ('upload_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.boyscategory')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
