# Generated by Django 4.2.1 on 2023-06-30 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reclaim', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account_recovery',
            name='username',
            field=models.CharField(default='susan', max_length=50),
        ),
    ]