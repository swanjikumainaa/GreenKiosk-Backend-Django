from django.db import models

# Create your models here.


class Shopping_cart(models.Model):
    user_id = models.IntegerField()
    products = models.CharField(max_length=32)
    total_price = models.DecimalField(max_digits = 6, decimal_places = 2)
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.user_id
    