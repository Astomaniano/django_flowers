# Generated by Django 5.1.3 on 2024-11-14 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_orders', '0003_remove_manageorder_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='manageorder',
            name='user_comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]