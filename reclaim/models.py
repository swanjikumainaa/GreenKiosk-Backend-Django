from django.db import models

# Create your models here.

class Account_recovery(models.Model):
    
    user_id = models.IntegerField()
    email = models.EmailField()
    
    
    def __str__(self):
        
        return self.user_id
