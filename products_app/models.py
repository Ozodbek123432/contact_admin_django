from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_price = models.IntegerField()
    product_sklad = models.BooleanField(default=False)
    product_size = models.FloatField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
