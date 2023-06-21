from django.db import models

# Create your models here.

class Payment(models.Model):
    user_id = models.IntegerField()
    order_id = models.IntegerField()
    payment_method = models.CharField()
    payment_amount = models.DecimalField(max_digits = 6, decimal_places = 2)
    transaction_id = models.IntegerField()
    
    
    def __str__(self):
        return self.user_id
    
    

