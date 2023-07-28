# Generated by Django 4.2.3 on 2023-07-07 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
        ('basket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopping_cart',
            name='customerName',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.RemoveField(
            model_name='shopping_cart',
            name='products',
        ),
        migrations.AddField(
            model_name='shopping_cart',
            name='products',
            field=models.ManyToManyField(to='inventory.product'),
        ),
    ]
