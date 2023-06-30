# Generated by Django 4.2.1 on 2023-06-30 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shopping_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('products', models.CharField(max_length=32)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
