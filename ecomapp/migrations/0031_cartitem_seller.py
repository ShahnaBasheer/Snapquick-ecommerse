# Generated by Django 4.1.1 on 2022-11-18 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0030_alter_cart_dlvry_chrg'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecomapp.seller'),
        ),
    ]