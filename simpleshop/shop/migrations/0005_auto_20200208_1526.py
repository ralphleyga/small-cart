# Generated by Django 3.0 on 2020-02-08 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_order_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Item',
        ),
        migrations.AddField(
            model_name='item',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Product'),
        ),
    ]
