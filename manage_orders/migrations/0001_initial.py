# Generated by Django 5.1.3 on 2024-11-14 12:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManageOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=20)),
                ('user_name', models.CharField(max_length=255)),
                ('user_surname', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('в работе', 'в работе'), ('передан в доставку', 'передан в доставку'), ('отмена', 'отмена')], max_length=255)),
                ('comment', models.TextField(blank=True)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
        ),
    ]