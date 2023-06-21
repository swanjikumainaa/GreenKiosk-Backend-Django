from django.db import models

# Create your models here.

class Search_engine(models.Model):
    user_id = models.IntegerField()
    search_query = models.TextField()
    results = models.TextField()
    timestamp = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.user_id
