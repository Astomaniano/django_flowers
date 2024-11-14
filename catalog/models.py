from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)  # Новое поле для изображения


    def __str__(self):
        return self.name