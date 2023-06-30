# Generated by Django 4.2.1 on 2023-06-30 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=6)),
                ('expiry_date', models.DateField(auto_now=True)),
                ('minimum_purchase', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
