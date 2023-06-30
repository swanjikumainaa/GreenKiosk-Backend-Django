from django.db import models

# Create your models here.

class Review(models.Model):
    user_id = models.CharField(max_length=50)
    product_id = models.CharField(max_length=50)
    rating = models.IntegerField()
    comment = models.TextField()
    
    
    def __str__(self):
        return self.user_id
    
    
