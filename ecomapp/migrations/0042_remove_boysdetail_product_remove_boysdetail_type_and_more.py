# Generated by Django 4.1.1 on 2022-11-28 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0041_alter_kidsfashion_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boysdetail',
            name='Product',
        ),
        migrations.RemoveField(
            model_name='boysdetail',
            name='Type',
        ),
        migrations.RemoveField(
            model_name='boysdetail',
            name='productdetail_ptr',
        ),
        migrations.RemoveField(
            model_name='boysfashion',
            name='age',
        ),
        migrations.RemoveField(
            model_name='boysfashion',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='boysfashion',
            name='category',
        ),
        migrations.RemoveField(
            model_name='boysfashion',
            name='size',
        ),
        migrations.RemoveField(
            model_name='girlsdetail',
            name='Product',
        ),
        migrations.RemoveField(
            model_name='girlsdetail',
            name='Type',
        ),
        migrations.RemoveField(
            model_name='girlsdetail',
            name='productdetail_ptr',
        ),
        migrations.RemoveField(
            model_name='girlsfashion',
            name='age',
        ),
        migrations.RemoveField(
            model_name='girlsfashion',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='girlsfashion',
            name='category',
        ),
        migrations.RemoveField(
            model_name='girlsfashion',
            name='size',
        ),
        migrations.DeleteModel(
            name='BoysCategory',
        ),
        migrations.DeleteModel(
            name='BoysDetail',
        ),
        migrations.DeleteModel(
            name='BoysFashion',
        ),
        migrations.DeleteModel(
            name='GirlsCategory',
        ),
        migrations.DeleteModel(
            name='GirlsDetail',
        ),
        migrations.DeleteModel(
            name='GirlsFashion',
        ),
    ]