from django.db import models

# Create your models here.

class Refunds(models.Model):
    order_id = models.IntegerField()
    refund_id = models.IntegerField()
    amount = models.DecimalField(max_digits = 6, decimal_places = 2)
    reason = models.TextField()
    status = models.CharField()
    request_date = models.DateTimeField(auto_now = True)
    processed_date = models.DateField(auto_now = True)
    
    def __str__(self):
        return self.order_id

#