# Generated by Django 3.0 on 2020-02-11 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='payment_method',
            field=models.IntegerField(choices=[(1, 'Cash on Delivery'), (3, 'Remittance')]),
        ),
    ]
