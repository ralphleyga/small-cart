# Generated by Django 3.0 on 2020-02-14 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20200211_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(1, 'Bag'), (3, 'Placed Order'), (4, 'Canceled')]),
        ),
    ]