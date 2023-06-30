from django.db import models

# Create your models here.

class Account_recovery(models.Model):
    username = models.CharField(max_length = 50, default='susan')    
    user_id = models.IntegerField()
    email = models.EmailField()
    
    
    def __str__(self):
        
        return self.username
