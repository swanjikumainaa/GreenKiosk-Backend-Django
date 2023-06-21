from django.db import models

# Create your models here.

class Review(models.Model):
    user_id = models.CharField()
    product_id = models.CharField()
    rating = models.IntegerField()
    comment = models.TextField()
    
    
    def __str__(self):
        return self.user_id
    
    
