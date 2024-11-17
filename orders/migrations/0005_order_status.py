# Generated by Django 5.1.3 on 2024-11-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_rename_comment_order_user_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('new', 'Новый'), ('notified', 'Уведомление отправлено'), ('completed', 'Завершен')], default='new', max_length=10),
        ),
    ]
