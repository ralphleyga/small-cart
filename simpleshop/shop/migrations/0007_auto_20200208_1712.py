# Generated by Django 3.0 on 2020-02-08 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20200208_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(1, 'Bag'), (2, 'Checkout'), (3, 'Paid'), (4, 'Canceled')]),
        ),
    ]
