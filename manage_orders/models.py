from django.db import models
from django.conf import settings

class ManageOrder(models.Model):
    order_id = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=[
        ('в работе', 'в работе'),
        ('передан в доставку', 'передан в доставку'),
        ('отмена', 'отмена'),
    ])
    user_comment = models.TextField(blank=True, null=True)
    manager_comment = models.TextField(blank=True, null=True)