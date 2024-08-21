from django.db import models

class SiteSetting(models.Model):
    image = models.ImageField(upload_to="banner/")
    caption = models.TextField
    
    def __str__(self):
                return self.caption