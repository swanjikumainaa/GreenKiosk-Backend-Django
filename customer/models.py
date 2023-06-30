from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    date_of_birth = models.DateTimeField(auto_now_add = True)
    date_registered = models.DateTimeField(auto_now = True) 
    
    
    def __str__(self):
        return self.first_name