# Generated by Django 5.1.3 on 2024-11-14 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='first_name',
            field=models.CharField(default='valera', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='last_name',
            field=models.CharField(default='Vas', max_length=255),
            preserve_default=False,
        ),
    ]
