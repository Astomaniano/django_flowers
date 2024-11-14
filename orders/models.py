from django.db import models
from django.conf import settings
from catalog.models import Product
from django.db.models.signals import post_save
from django.dispatch import receiver
from manage_orders.models import ManageOrder

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    user_comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"Order #{self.id} by {self.user}"

@receiver(post_save, sender=Order)
def create_manage_order(sender, instance, created, **kwargs):
    if created:
        ManageOrder.objects.create(
            order_id=instance,
            phone_number=instance.phone_number,
            first_name=instance.first_name,
            last_name=instance.last_name,
            user_comment=instance.user_comment,
        )

