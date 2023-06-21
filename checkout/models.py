from django.db import models

# Create your models here.

class Order(models.Model):
    userId = models.IntegerField()
    products = models.ManyToManyField("app.Model", verbose_name= ("my_products"))
    total_price = models.DecimalField(max_digits = 6, decimal_places = 2)
    shipping_address = models.CharField(max_length=50)
    order_date = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.userId
    
    


