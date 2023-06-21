from django.db import models

# Create your models here.
class Create_account(models.Model):
    user_id = models.CharField()
    username = models.CharField()
    email = models.EmailField()
    firstName = models.CharField()
    lastname = models.CharField()
    date_of_birth = models.CharField()
    phone_number = models.CharField()
    address = models.CharField()
    
    def __str__(self):
        return self.user_id
    
    

