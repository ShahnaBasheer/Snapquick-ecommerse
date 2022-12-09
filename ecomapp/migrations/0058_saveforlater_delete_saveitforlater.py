# Generated by Django 4.1.3 on 2022-12-04 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecomapp', '0057_ecomcart_ecomcartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaveForLater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='')),
                ('title', models.CharField(max_length=60, null=True)),
                ('qty', models.IntegerField(default=1)),
                ('price', models.IntegerField()),
                ('mrp', models.IntegerField(default=0)),
                ('all_pro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.allfashion')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.brand')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.seller')),
                ('size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecomapp.size')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='SaveItForLater',
        ),
    ]
