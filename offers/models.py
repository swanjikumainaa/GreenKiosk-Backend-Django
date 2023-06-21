from django.db import models

# Create your models here.


class Discounts(models.Model):
    code = models.IntegerField()
    percentage = models.DecimalField(max_digits = 6, decimal_places = 2)
    expiry_date = models.DateField(auto_now = True)
    minimum_purchase = models.DecimalField(max_digits = 6, decimal_places = 2)
    
    def __str__(self):
        return self.code
    
    
  