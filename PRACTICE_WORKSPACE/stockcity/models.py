from django.db import models

class Product(models.Model):
    Title = models.CharField(max_length=500)
    #Date = models.FloatField()
    Date = models.CharField(max_length=50)
    Description = models.CharField(max_length=50000)
    def __str__(self):   #in browser in admin mode to make visible both product name and data or it can be name and id
        return f"{self.Title} ({self.Date})"  #or also use return f"{self.Title} ({self.id})"

# Create your models here.
