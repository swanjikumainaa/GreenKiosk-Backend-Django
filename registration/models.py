from django.db import models

# Create your models here.
class Create_account(models.Model):
    user_id = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    date_of_birth = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    
    def __str__(self):
        return self.user_id
    
    

