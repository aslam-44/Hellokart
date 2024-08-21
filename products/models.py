from django.db import models


class Product(models.Model):
    LIVE = 1
    DELETE = 0

    DELETE_CHOICES = [
        (LIVE, 'Live'),
        (DELETE, 'Delete'),
    ]

    title = models.CharField(max_length=255)
    price = models.IntegerField()  
    description = models.TextField()  
    image = models.ImageField(upload_to="products/")
    priority = models.IntegerField(default=0)  
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at= models.DateTimeField(auto_now_add=True) 
    updated-at = models.DateTimeField(auto_now=True) 

    
    def __str__(self):
                return self.title