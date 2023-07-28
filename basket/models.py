from django.db import models
from inventory.models import Product

# Create your models here.


class Shopping_cart(models.Model):
    customerName = models.CharField(max_length=32, default = '')
    products = models.ManyToManyField(Product) 
    user_id = models.IntegerField()
    total_price = models.DecimalField(max_digits = 6, decimal_places = 2)
    quantity = models.IntegerField()


    
    
    def __str__(self):
        return self.customerName
    